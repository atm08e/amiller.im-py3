import json
import logging
import pprint
import sys
import os
import routes
#
from aiohttp import web
import aiohttp_jinja2
from aiohttp_jinja2 import jinja2
#
from handlers.handlers import Handlers
from helpers.gallery_json_loader import gallery_json_loader

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)


class AmillerIm:
    @staticmethod
    def get_app(**kwargs):
        # Create base web application
        app = web.Application(loop=kwargs.get('loop'))

        # Setup web application paths
        app['path_to_app_root'] = os.path.dirname(os.path.abspath(__file__))
        app['path_to_templates'] = '{}/{}'.format(app['path_to_app_root'], 'templates')
        app['path_to_static'] = '{}/{}'.format(app['path_to_app_root'], 'static')

        # Load galleries into memory
        app['galleries'] = {
            'snowboarding':
                {
                    '2016':
                    {
                        '1': gallery_json_loader(
                                os.path.join(app['path_to_static'],
                                             *['galleries', 'snowboarding', '2016', 'wreckbreck2016.json'])),
                        '2': gallery_json_loader(
                                os.path.join(app['path_to_static'],
                                             *['galleries', 'snowboarding', '2016', 'familybreck2016.json']))
                    },
                    '2017':
                    {
                        '1': gallery_json_loader(
                                os.path.join(app['path_to_static'],
                                             *['galleries', 'snowboarding', '2017', 'wreckbreck2017.json'])),
                        '2': gallery_json_loader(
                                os.path.join(app['path_to_static'],
                                             *['galleries', 'snowboarding', '2017', 'shredapalooza2017.json'])),
                        '3': gallery_json_loader(
                                os.path.join(app['path_to_static'],
                                             *['galleries', 'snowboarding', '2017', 'brecksolo2017.json'])),
                    }
                }
        }

        aiohttp_jinja2.setup(app,
                             context_processors=[aiohttp_jinja2.request_processor],
                             loader=jinja2.FileSystemLoader(app['path_to_templates']))

        routes.setup(app=app, handler=Handlers)
        return app


def main():
    port = int(os.getenv('PORT', '5000'))
    logger.debug('Will try to start server on {}'.format(port))
    web.run_app(AmillerIm.get_app(), port=port)


if __name__ == '__main__':
    main()
