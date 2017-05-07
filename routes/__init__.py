def setup(app, handler, *args, **kwargs):

    # Application Routes
    app.router.add_get('/', handler.root)
    app.router.add_get('/snowboarding/{year}/{trip}', handler.snowboarding)
    app.router.add_get('/fishing/{trip}', handler.snowboarding)
    app.router.add_get('/about', handler.about)
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