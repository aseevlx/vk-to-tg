import logging

import requests

from settings import BOT_API_TOKEN, TG_CHAT_ID

logger = logging.getLogger('tg_logger')
POST_URL = f'https://api.telegram.org/bot{BOT_API_TOKEN}/sendPhoto?chat_id={TG_CHAT_ID}&photo='


def send_photo_to_channel(photo_url):
    """
    Send message to channel
    :param photo_url: string
    :return:
    """
    logger.info(f'Sending picture with url {photo_url} to channel')
    try:
        url = POST_URL + photo_url
        response = requests.post(url)
        logger.debug(response)
    except BaseException as e:
        logger.critical(f'Error sending: {e}')
