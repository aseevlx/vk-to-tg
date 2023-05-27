# vk-to-tg
App for automatic repost photos from vk group to telegram channel.

## deploy
1) Clone repository
2) Get token for telegram bot from [@BotFather](https://t.me/BotFather).
3) Create standalone VK app, get its id and service token
4) Get your vk group id
5) Type `pipenv install`
6) Copy .env.conf file to .env and fill it with your data.
7) Init db: `python initdb.py`
8) Type `chmod +x ./run.py`
9) Add script to cronab

## .env variables
* `BOT_API_TOKEN` - token from @BotFather
* `TG_CHAT_ID` - telegram group name, should start from @
* `VK_APP_ID` - vk app id
* `VK_SERVICE_TOKEN` - vk service app token
* `VK_PAGE_ID` - vk group id for tracking, should start from -
* `POSTS_COUNT` - count of posts will fetched from vk by every iteration
* `DB_PATH` - path to sqlite db
* `SETTINGS_MODULE` - prod or dev
* `PROJECT_PATH` - path to root of project

Params for base init
* `TG_CHANNEL_NAME` 
* `TG_CHANNEL_URL`
* `VK_PUBLIC_NAME`
* `VK_PUBLIC_URL`

## Checks
Install dev dependencies: `pipenv install --dev`
Then run checks:

* black:
  * `pipenv run black . --config pyproject.toml`
* flake8
  * `pipenv run flake8 . --toml-config pyproject.toml`