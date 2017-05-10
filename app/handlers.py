import logging
import sys

import aiohttp_jinja2

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Handlers:

    @aiohttp_jinja2.template('index.html')
    async def root(request):
        context = {'name': 'Andrew', 'surname': 'Svetlov'}
        response = aiohttp_jinja2.render_template('index.html',
                                                  request,
                                                  context)
        response.headers['amiller.im-custom'] = 'en'
        return response

    @aiohttp_jinja2.template('about.html')
    async def about(request):
        return {'about': 'derp'}

    @aiohttp_jinja2.template('links.html')
    async def links(request):
        return {'about': 'derp'}

    @aiohttp_jinja2.template('blog.html')
    async def blog(request):
        return {'about': 'derp'}

    @aiohttp_jinja2.template('login.html')
    async def login(request):
        return {'about': 'derp'}

    @aiohttp_jinja2.template('register.html')
    async def register(request):
        return {'about': 'derp'}

    @aiohttp_jinja2.template('snowboarding.html')
    async def snowboarding(request):
        year = request.match_info.get('year', None)
        trip = request.match_info.get('trip', None)
        # TODO check year and default
        #logger.debug(request.app['galleries']['snowboarding'])
        gallery = request.app['galleries']['snowboarding'][year][trip]

        return gallery

    @aiohttp_jinja2.template('under_construction.html')
    async def under_construction(request):
        return {'about': 'derp'}

    @aiohttp_jinja2.template('under_construction.html')
    async def test(request):
        return {'about': 'derp'}