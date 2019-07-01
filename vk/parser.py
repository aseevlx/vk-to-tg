import logging
from datetime import datetime

from vk_api import vk_api

from .helpers import get_only_new_posts

from settings import VK_APP_ID, VK_SERVICE_TOKEN

from vk.models import VkPublic
from tg.models import TgChannel, TgPost


def get_new_posts():
    """
    Fetch and parse posts from vk
    :return:
    """
    logging.info('Fetch posts from VK')

    check_date = datetime.now()
    vk_public = VkPublic.get_by_id(1)  # FIXME: hardcode
    tg_channel = TgChannel.get_by_id(1)  # FIXME: hardcode

    try:
        vk_session = vk_api.VkApi(app_id=VK_APP_ID, token=VK_SERVICE_TOKEN)
        vk = vk_session.get_api()

        # TODO: use vk.execute to get posts from date
        posts = vk.wall.get(owner_id=vk_public.page_id, count=vk_public.posts_count).get('items')
        import ipdb;ipdb.set_trace()
        posts = get_only_new_posts(posts, vk_public)
        logging.info(f'Fetched {len(posts)} new posts')
    except BaseException as e:
        logging.error(f'Error fetching new posts: {e}')
        return

    for post in posts:
        parse_and_save_post(post, vk_public, tg_channel)

    vk_public.last_check_date = check_date
    vk_public.save()


def parse_and_save_post(post, vk_public, tg_channel):
    """
    Save TgPost object
    :param post: dict
    :param vk_public: VkPublic object
    :param tg_channel: TgChannel object
    :return:
    """
    TgPost(
        post_id=post.get('id'),  # unique identifier of vk post
        pictures=get_photos(post),  # TODO: нужно учитывать, что в репостнутом скорее всего картинка, нужно брать их из репоста!
        text=post.get('text'),
        reposted_from=get_url_to_reposted_post(post),
        reposted_text=get_reposted_text(post),
        reposted_pictures=get_reposted_pictures(post),
        sent=False,
        vk_public=vk_public,
        tg_channel=tg_channel
    ).save()


def get_photos(post):
    """
    Parse photo urls from post
    and return string with photo urls
    :param post: dict
    :return: list
    """
    photos = []
    sizes_range = ['w', 'z', 'y', 'x', 'm']  # preferred sizes of pics, from bigger to smaller

    attachments = post.get('attachments')
    if attachments is None:
        return ''

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

    return ','.join(photos)


def get_url_to_reposted_post(post):
    """
    Get url to reposted post
    :param post: dict
    :return: str
    """
    if not post.get('copy_history'):
        return ''

    from_id = post['copy_history'][0]['from_id']
    post_id = post['copy_history'][0]['id']

    return f'https://vk.com/wall{from_id}_{post_id}'


def get_reposted_text(post):
    """
    Get text of reposted post
    :param post: dict
    :return: str
    """
    if not post.get('copy_history'):
        return ''

    return post['copy_history'][0]['text']


def get_reposted_pictures(post):
    """

    :return:
    """
    return ''
