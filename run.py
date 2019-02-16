#!/usr/bin/env pipenv run python
import signal
from threading import Event
import logging

from vk_parser import send_posts

from settings import PARSING_INTERVAL

exit_event = Event()
running = True


def main():
    while not exit_event.is_set():
        send_posts()
        exit_event.wait(PARSING_INTERVAL)


def quit(signo, _frame):
    logging.info(f'Interrupted by {signo}, shutting down')
    exit_event.set()


if __name__ == '__main__':
    for sig in ('TERM', 'HUP', 'INT'):
        signal.signal(getattr(signal, 'SIG' + sig), quit)

    logging.info('Starting app loop')

    main()
