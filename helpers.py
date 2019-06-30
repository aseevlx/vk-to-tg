import shelve
from time import time


def get_last_post_date():
    """
    Get last post date from shelve if exists
    Else - save current date and return it
    :return: int
    """
    with shelve.open('db.txt') as db:
        last_post_date = db.get('last_post_date')

        if last_post_date is None:
            db['last_post_date'] = int(time())
            last_post_date = db['last_post_date']

    return last_post_date


def update_last_post_date():
    """
    Get last post date from shelve
    :param last_post_date:
    :return:
    """
    with shelve.open('db.txt') as db:
        db['last_post_date'] = int(time())
