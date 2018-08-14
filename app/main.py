#!/usr/bin/env python3

#
import asyncio
import uvloop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
#
import datetime
import logging
import sys
import base64
from pathlib import Path
#
import aiohttp_session
import aiohttp_jinja2
from aiohttp import web
from aiohttp_jinja2 import jinja2
from aiohttp_session.cookie_storage import EncryptedCookieStorage
#
from app.blogs import setup_blogs
from app.galleries import setup_galleries
from app.handlers import Handlers
from app.routes import setup_routes
from app.settings import Settings

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)
#
APP_DIR = Path(__file__).parent
ROOT_DIR = APP_DIR.parent
STATIC_DIR = str(ROOT_DIR / 'static')
TEMPLATE_DIR = str(APP_DIR / 'templates')


async def on_startup(app: web.Application):
    # Mongo Connection
    # app['mongo'] = None
    pass

async def on_cleanup(app: web.Application):
    # Clean up Mongo Connection
    # app['mongo'] = None
    pass


async def create_app():
    # Create base web application
    app = web.Application()

    # Settings
    settings = Settings()

    # Setup web application paths
    app.update(
        name='amiller.im',
        settings=settings,
        #
        path_to_app_root=APP_DIR,
        path_to_templates=TEMPLATE_DIR,
        path_to_static=STATIC_DIR,
        #
        # blogs=setup_blogs(STATIC_DIR),
        galleries=setup_galleries(STATIC_DIR),
        #
        deployment_time='{:%b, %d %Y %H:%M:%S}'.format(datetime.date.today())
    )

    # Template Engine
    aiohttp_jinja2.setup(app,
                         context_processors=[aiohttp_jinja2.request_processor],
                         loader=jinja2.FileSystemLoader(TEMPLATE_DIR))

    # Pre and Post Application Hooks
    app.on_startup.append(on_startup)
    app.on_cleanup.append(on_cleanup)

    # Sessions
    secret_key = base64.urlsafe_b64decode(settings.COOKIE_SECRET)
    aiohttp_session.setup(app, EncryptedCookieStorage(secret_key))

    # Routes
    setup_routes(app=app, handler=Handlers)

    return app
