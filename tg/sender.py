import logging
import textwrap
from io import BytesIO
from typing import Optional

import requests
from telegram import InputMediaPhoto

from settings import bot
from tg.helpers import get_repost_text
from tg.models import TgChannel, TgPost

logger = logging.getLogger("tg_logger")


def send_new_posts():
    """
    Get new posts
    """
    tg_channel = TgChannel.get_by_id(1)  # FIXME: hardcode for one channel
    new_posts = TgPost.select().where(TgPost.sent == False, TgPost.tg_channel == tg_channel)  # noqa: E712

    for post in new_posts:
        try:
            send_post_to_channel(tg_channel.chat_id, post)
        except BaseException as e:
            logger.critical(f"Can't send post {post.id}: {e}")


def send_post_to_channel(chat_id: str, post: TgPost):
    logger.info(f"Sending post with id {post.post_id} to channel {chat_id}")

    post_to_reply = None
    try:
        if post.reposted_from:
            post_to_reply = send_repost(chat_id, post)
        if post.pictures:
            send_post_with_pics(chat_id, post.pictures, post.text, post_to_reply)
        elif post.text:
            send_post_with_text(chat_id, post.text, post_to_reply)
        else:
            logger.critical(f"Can't recognize post type with id {post.post_id}")
    except BaseException as e:
        logger.critical(f"Can't send post {post.id}: {e}")

    post.sent = True
    post.save()


def send_repost(chat_id: str, post: TgPost) -> str:
    """
    Send repost with picture(s) or text
    FIXME: Add an exception catch due to issues with uploading images to TG
    """
    text = get_repost_text(post)
    message_id = None

    if post.reposted_pictures:
        message_id = send_post_with_pics(chat_id, post.reposted_pictures, text)
    elif text:
        message_id = bot.send_message(chat_id=chat_id, text=text)

    return message_id


def send_post_with_pics(chat_id: str, pictures: str, text: str, post_to_reply: Optional[str] = None) -> Optional[str]:
    """
    Send a post containing photos
    """
    pictures_list = pictures.split(",")
    message_id = None

    # VK post, as well as Telegram, can contain only 10 photos
    if 1 < len(pictures_list) <= 10:
        if len(text) > 1024:
            send_post_with_text(chat_id, text, post_to_reply)
            text = ""

        pictures = []
        for picture_url in pictures_list:
            try:
                pic = BytesIO(requests.get(picture_url).content)
            except BaseException as e:
                logger.error(f"Error downloading picture: {e}")
                continue

            pictures.append(InputMediaPhoto(media=pic, caption=text))

        message_id = bot.send_media_group(chat_id=chat_id, media=pictures, reply_to_message_id=post_to_reply)[
            0
        ].message_id
    elif len(pictures_list) == 1:
        # maximum length of caption is 1024 symbols
        if len(text) > 1024:
            send_post_with_text(chat_id, text, post_to_reply)
            text = ""

        try:
            pic = BytesIO(requests.get(pictures_list[0]).content)
        except BaseException as e:
            logger.error(f"Error downloading picture: {e}")
            return

        message_id = bot.send_photo(
            chat_id=chat_id, photo=pic, caption=text, reply_to_message_id=post_to_reply
        ).message_id

    return message_id


def send_post_with_text(chat_id: str, text: str, post_to_reply: Optional[str] = None) -> Optional[str]:
    """
    Send text message.
    If length of text > 4096, send multiple messages
    """
    message_id = None

    # max length of one TG message is 4096 symbols
    if 0 < len(text) <= 4096:
        message_id = bot.send_message(
            chat_id=chat_id, text=text, disable_web_page_preview=True, reply_to_message_id=post_to_reply
        ).message_id

    if len(text) > 4096:
        text_list = textwrap.wrap(text, 4096)
        for text_piece in text_list:
            message_id = bot.send_message(
                chat_id=chat_id, text=text_piece, disable_web_page_preview=True, reply_to_message_id=post_to_reply
            ).message_id

    return message_id
