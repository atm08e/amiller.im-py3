# pylint: disable=no-member
import logging
import sys

import aiohttp_jinja2

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Handlers(object):

    @aiohttp_jinja2.template('index.html')
    async def root(self):
        context = {'name': 'Andrew', 'surname': 'Svetlov'}
        response = aiohttp_jinja2.render_template('index.html',
                                                  self,
                                                  context)
        response.headers['amiller.im-custom'] = 'en'
        return response

    @aiohttp_jinja2.template('about_drew.html')
    async def about_drew(self):
        return {'about': 'derp'}

    @aiohttp_jinja2.template('about_site.html')
    async def about_site(self):
        return {'about': 'derp'}

    @aiohttp_jinja2.template('links.html')
    async def links(self):
        return {'about': 'derp'}

    @aiohttp_jinja2.template('blog.html')
    async def blog(self):
        return {'about': 'derp'}

    @aiohttp_jinja2.template('login.html')
    async def login(self):
        return {'about': 'derp'}

    @aiohttp_jinja2.template('register.html')
    async def register(self):
        return {'about': 'derp'}

    @aiohttp_jinja2.template('blog.html')
    async def movies(self):
        name = self.match_info.get('name', None)
        return self.app['blogs']['movies'][name]

    @aiohttp_jinja2.template('gallery.html')
    async def snowboarding(self):
        year = self.match_info.get('year', None)
        trip = self.match_info.get('trip', None)
        # TODO check year and default
        #logger.debug(self.app['galleries']['snowboarding'])
        return self.app['galleries']['snowboarding'][year][trip]

    @aiohttp_jinja2.template('gallery.html')
    async def boating(self):
        year = self.match_info.get('year', None)
        trip = self.match_info.get('trip', None)
        # TODO check year and default
        return self.app['galleries']['boating'][year][trip]

    @aiohttp_jinja2.template('under_construction.html')
    async def under_construction(self):
        return {'about': 'derp'}

    @aiohttp_jinja2.template('under_construction.html')
    async def test(self):
        return {'about': 'derp'}
