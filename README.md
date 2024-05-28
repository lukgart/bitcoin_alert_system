# Bitcoin Price Tracker and Alert System with Telegram Alerts

## Description
This script fetches the latest Bitcoin prices from an API and sends alerts via Telegram when the price crosses a certain threshold.

## Features
- Fetch current Bitcoin price from a reliable API (e.g., CoinGecko, CoinMarketCap).
- Set price thresholds for alerts.
- Send alerts via Telegram using the Telegram Bot API.


#
## How to Set Up
#
### Create a Telegram Bot:
1. Search for the “BotFather” on Telegram.
2. Start a chat with the BotFather and create a new bot using the `/newbot` command.
3. Follow the prompts to set up your bot and get the bot token.

### Get Your Chat ID:
1. Start a chat with your bot and send any message.
2. Visit `https://api.telegram.org/bot<your_bot_token>/getUpdates` in your browser (replace `<your_bot_token>` with your actual bot token).
3. Look for the `chat` object in the JSON response to find your chat ID.

### Replace the Placeholder Values:
1. Replace `your_telegram_bot_token` with the token you got from the BotFather.
2. Replace `your_chat_id` with your chat ID.
