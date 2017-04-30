import aiohttp_jinja2


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

@aiohttp_jinja2.template('under_construction.html')
async def snowboarding(request):
    year = request.match_info.get('year', None)

@aiohttp_jinja2.template('under_construction.html')
async def under_construction(request):
    return {'about': 'derp'}