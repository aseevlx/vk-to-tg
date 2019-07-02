#!/usr/bin/env python3.7
from vk.parser import get_new_posts
from tg.sender import send_new_posts


if __name__ == '__main__':
    get_new_posts()
    send_new_posts()
