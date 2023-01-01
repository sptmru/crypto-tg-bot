# Crypto Bot

## Create the virtual environment

Create the dev virtual environment:

```bash
./create-venv 1
```

Create the virtual environment:

```bash
./create-venv
```

## Start

Paste the necessary data in `.env`:

```
TELEGRAM_BOT_API_TOKEN=
TELEGRAM_ADMIN_ID=

WEBHOOK_HOST=
WEBHOOK_PATH=
WEBHOOK_URL=${WEBHOOK_HOST}${WEBHOOK_PATH}

WEBAPP_HOST=
WEBAPP_PORT=
```

To start:

```bash
./start
```
