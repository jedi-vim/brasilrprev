#!/bin/bash
python -m brprev_bot.cli
gunicorn -w 2 -b 0.0.0.0:4000 'brprev_bot.app:create_app()'
