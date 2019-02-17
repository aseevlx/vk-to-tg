import logging

from vk_api import vk_api

from tg_sender import send_photo_to_channel
from settings import VK_APP_ID, VK_SERVICE_TOKEN, VK_PAGE_ID, POSTS_COUNT
from helpers import get_last_post_date, update_last_post_date


def send_posts():
    """
    Authorize, get posts from wall and parse photo urls
    :return:
    """
    logging.info('Fetch posts from VK')
    try:
        vk_session = vk_api.VkApi(app_id=VK_APP_ID, token=VK_SERVICE_TOKEN)
        vk = vk_session.get_api()

        posts = vk.wall.get(owner_id=VK_PAGE_ID, count=POSTS_COUNT)
        photos = get_photos(posts['items'])

        for photo_url in photos:
            send_photo_to_channel(photo_url)
    except Exception as e:
        logging.error(f'Error sending posts: {e}')

    photos_sent = len(photos)
    logging.info(f'{photos_sent} posts was sent')


def get_photos(posts):
    """
    Parse photo urls from posts
    and return it in reverse order (from older to newest)
    :param posts: dict
    :return: list
    """
    photos = []
    sizes_range = ['w', 'z', 'y', 'x', 'm']
    last_send_date = get_last_post_date()
    for post in posts:
        # continue loop if post was posted before
        if post['date'] <= last_send_date:
            continue

        photo_sizes = {}
        attachments = post.get('attachments')
        if attachments is None:
            continue

        for attachment in attachments:
            if attachment['type'] != 'photo':
                continue
            # get all photo sizes
            photo_sizes = {photo['type']: photo['url'] for photo in attachment['photo']['sizes']}

        # get image with maximal resolution
        for size in sizes_range:
            if photo_sizes.get(size) is not None:
                photos.append(photo_sizes[size])
                break

    if photos:
        update_last_post_date()
    return photos[::-1]
