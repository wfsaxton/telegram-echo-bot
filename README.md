# telegram-echo-bot

A simple echo bot for Telegram using ngrok and FastAPI

# Installation

## Install ngrok

```
curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc |
sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" |
sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok
ngrok config add-authtoken 2cgXKDhDfoVZwO4e2bM9vx1xWT2_7NLGUMPFin5pwfAwqAVta
ngrok http 5000
```

## Configure the bot to use ngrok

Copy the URL from the ngrok terminal and paste it in the `.env` file WEBHOOK_URL

## Create a bot token

Visit https://telegram.me/BotFather and run the /newbot command. Follow the instructions to create a bot. You will receive a token to access the HTTP API. Copy this token and paste it in the `.env` file TELEGRAM_TOKEN

## Setup Python environment

```
pdm install
```

## Run telegram bot

```
pdm run uvicorn src.telegram_echo_bot.echo_bot:app --reload --port 5000
```
