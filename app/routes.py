import logging

import sys

from aiohttp import web

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)


def setup_routes(app: web.Application, handler):
    # Application Routes
    app.router.add_get('/', handler.root)
    app.router.add_get('/snowboarding/{year}/{trip}', handler.snowboarding)
    app.router.add_get('/fishing/{trip}', handler.snowboarding)
    app.router.add_get('/about/drew', handler.about_drew)
    app.router.add_get('/about/site', handler.about_site)
    app.router.add_get('/blog', handler.blog)
    app.router.add_get('/blog/{name}', handler.blog)
    app.router.add_get('/links', handler.links)
    app.router.add_get('/register', handler.register)
    app.router.add_get('/login', handler.login)
    app.router.add_get('/under_construction', handler.under_construction)
    app.router.add_get('/test', handler.test)

    # Static Routes
    app.router.add_static(prefix='/static/',
                          path=app['path_to_static'],
                          name='static')
