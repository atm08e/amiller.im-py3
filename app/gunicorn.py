"""
For Production

gunicorn app.gunicorn:app --worker-class aiohttp.worker.GunicornWebWorker
"""

import asyncio

from .main import create_app

LOOP = asyncio.get_event_loop()
APP = create_app(LOOP)
