import logging
import textwrap

from telegram import InputMediaPhoto

from settings import bot
from tg.helpers import get_post_text
from tg.models import TgChannel, TgPost

logger = logging.getLogger('tg_logger')


def send_new_posts():
    """
    Get new posts
    """
    channel = TgChannel.get_by_id(1)  # FIXME: hardcode for one channel
    new_posts = TgPost.select(sent=False, channel=channel)
    for post in new_posts:
        try:
            send_post_to_channel(channel.chat_id, post)
        except BaseException as e:
            logger.critical(f'Can\'t send post {post.id}: {e}')


def send_post_to_channel(chat_id, post):
    """
    Send one post to channel by type
    :param chat_id: str
    :param post: TgPost object
    """
    logger.info(f'Start sending post with id {post.id} to channel {chat_id}')

    if post.pictures:
        send_post_with_pics(chat_id, post)
    elif post.text or post.reposted_text:
        send_post_with_text(chat_id, post)
    else:
        logger.critical(f'Can\'t recognize post type with id {post.id}')
    post.sent = True
    post.save()


def send_post_with_pics(chat_id, post):
    pictures_list = post.pictures.split(',')
    text = get_post_text(post)

    # VK post, as well as Telegram, can contain only 10 photos
    if 1 < len(pictures_list) <= 10:
        pictures = []
        for picture_url in pictures_list:
            pictures.append(InputMediaPhoto(media=picture_url, caption=text))
            text = None

        bot.send_media_group(chat_id=chat_id, media=pictures)
        return
    elif len(pictures_list) == 1:
        bot.send_photo(chat_id=chat_id, photo=pictures_list[0], caption=text)  # maximum length of capture is 1024 symbols
        return


def send_post_with_text(chat_id, post):
    """
    Send text message.
    If length of text > 4096, send multiple messages
    :param chat_id: str
    :param post: TgPost object
    :return:
    """
    text = get_post_text(post)
    if 0 < len(text) <= 4096:
        bot.send_message(chat_id=chat_id, text=text)

    if len(text) > 4096:
        text_list = textwrap.wrap(text, 4096)
        for text in text_list:
            bot.send_message(chat_id=chat_id, text=text)

    return


