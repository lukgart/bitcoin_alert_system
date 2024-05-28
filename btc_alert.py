import requests

# Replace with your Telegram bot token and chat ID
TELEGRAM_BOT_TOKEN = 'your_telegram_bot_token'
TELEGRAM_CHAT_ID = 'your_chat_id'

# Function to send a message via Telegram
def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    response = requests.post(url, json=payload)
    return response.json()

# Function to fetch Bitcoin price
def get_bitcoin_price():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    return data['bitcoin']['usd']

# Main function
if __name__ == '__main__':
    price_threshold = 30000  # Set your price threshold here
    price = get_bitcoin_price()
    print(f'Current Bitcoin price: ${price}')
    if price > price_threshold:
        message = f'Bitcoin price alert! Current price: ${price}'
        send_telegram_message(message)
