import logging
import sys
import handlers
import os
import routes
#
from aiohttp import web
import aiohttp_jinja2
from aiohttp_jinja2 import jinja2


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)


class AmillerIm:
    @staticmethod
    def get_app(**kwargs):

        app = web.Application(loop=kwargs.get('loop'))
        app['path_to_app_root'] = os.path.dirname(os.path.abspath(__file__))
        app['path_to_templates'] = '{}/{}'.format(app['path_to_app_root'], 'templates')
        app['path_to_static'] = '{}/{}'.format(app['path_to_app_root'], 'static')

        aiohttp_jinja2.setup(app,
                             context_processors=[aiohttp_jinja2.request_processor],
                             loader=jinja2.FileSystemLoader(app['path_to_templates']))

        routes.setup(app=app, handler=handlers)
        return app


def main():
    port = int(os.getenv('PORT', '5000'))
    logger.debug('Will try to start server on {}'.format(port))
    web.run_app(AmillerIm.get_app(), port=port)

if __name__ == '__main__':
    main()
