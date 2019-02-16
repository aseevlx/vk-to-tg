# vk-to-tg
App for automatic repost photos from vk group to telegram channel.

## Deploy
1) Clone repository
2) Get token for telegram bot from [@BotFather](https://t.me/BotFather).
3) Create standalone VK app, get its id and service token
4) Get your vk group id
5) Type `pipenv install`
6) Copy .env.conf file to .env and fill it with your data.

## .env variables
* `BOT_API_TOKEN` - token from @BotFather
* `TG_CHAT_ID` - telegram group name, should start from @
* `VK_APP_ID` - vk app id
* `VK_SERVICE_TOKEN` - vk service app token
* `VK_PAGE_ID` - vk group id for tracking, should start from -
* `POSTS_COUNT` - count of posts will fetched from vk by every iteration 