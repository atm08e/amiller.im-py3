import logging
import sys
import handlers
import os
import routes
#
from aiohttp import web as web
from aiohttp_jinja2 import jinja2 as jinja2
from aiohttp_jinja2 import aiohttp_jinja2 as aiohttp_jinja2


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)


class AmillerIm:
    @staticmethod
    def get_app(**kwargs):
        app = web.Application(loop=kwargs.get('loop'))

        path_to_templates = '/home/amiller/workspace/amiller.im/templates'
        aiohttp_jinja2.setup(app,
                             context_processors=[aiohttp_jinja2.request_processor],
                             loader=jinja2.FileSystemLoader(path_to_templates))

        routes.setup(app=app, handler=handlers)
        return app


def main():
    port = int(os.getenv('PORT', '5000'))
    logger.debug('Will try to start server on {}'.format(port))
    web.run_app(AmillerIm.get_app(), port=port)

if __name__ == '__main__':
    main()
