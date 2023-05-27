import time
from datetime import datetime


def get_only_new_posts(posts, vk_public):
    """
    Compare post date with last check date
    and return only new posts
    :param posts: list
    :param vk_public: VkPublic object
    :return: list
    """
    if not posts:
        return

    last_check_date = vk_public.last_check_date
    new_posts = []

    for post in posts:
        post_date = utc2local(datetime.utcfromtimestamp(post["date"]))
        if post_date < last_check_date:
            continue
        new_posts.append(post)

    return new_posts[::-1]


def utc2local(utc_time):
    epoch = time.mktime(utc_time.timetuple())
    offset = datetime.fromtimestamp(epoch) - datetime.utcfromtimestamp(epoch)
    return utc_time + offset
