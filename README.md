# urdango-capstone-project
The project is undertaken as part of academic curriculum.

## Requirements

1. `pip install django-cors-headers`
2. `pip install channels`
3. `pip install daphne`
4. `pip install httpx`

## Setup
1. Run `daphne urdango.asgi:application` to test WebSocket connection otherwise just `python manage.py runserver`

## VAPID Setup
1. Run `npm install web-push -g` then
2. `web-push generate-vapid-keys`
3. Set up the environment variables for the key pair as
`PUBLIC_VAPID_KEY` and `PRIVATE_VAPID_KEY` in `/urdango/.env` (same level as `settings.py`)