"""
For Production

gunicorn app.gunicorn:app --worker-class aiohttp.worker.GunicornWebWorker
"""

import asyncio

from .main import create_app

loop = asyncio.get_event_loop()
app = create_app(loop)
