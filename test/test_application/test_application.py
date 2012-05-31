import unittest
import rest
import rest.application
import rest.response
import werkzeug as werk


urls = {
    '/': 'Index',
    '/<int:test>': 'IndexWithParam'
}


class Index(object):
    def GET(self, request):
        return rest.response.ok('Works.')


class IndexWithParam(object):
    def GET(self, request, test):
        return rest.response.ok(test)

    def POST(self, request, test):
        return rest.response.created(request.data)


class TestRestApplication(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_application_can_be_created(self):
        app = rest.application.Application(urls, globals())

    def test_application_is_callable(self):
        app = rest.application.Application(urls, globals())
        env = werk.EnvironBuilder(path='/', method='GET')
        env = env.get_environ()
        start_response = lambda *args, **kwargs: None
        app(env, start_response)

    def test_application_returns_an_iterable(self):
        app = rest.application.Application(urls, globals())
        env = werk.EnvironBuilder(path='/', method='GET')
        env = env.get_environ()
        start_response = lambda *args, **kwargs: None
        response = app(env, start_response)
        self.assertIs(hasattr(response, 'next'), True)
        self.assertIs(hasattr(response, 'close'), True)

    def test_appliction_can_simulate_request(self):
        app = rest.application.Application(urls, globals())
        response = app.request()

    def test_application_sim_request_returns_response(self):
        app = rest.application.Application(urls, globals())
        response = app.request()
        self.assertIs(isinstance(response, werk.Response), True)

    def test_application_sim_response_contains_correct_values(self):
        app = rest.application.Application(urls, globals())
        response = app.request()
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.data, 'Works.')

    def test_application_passes_kwargs(self):
        app = rest.application.Application(urls, globals())
        response = app.request(url='/1234')
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.data, '1234')

    def test_application_handles_verbs(self):
        app = rest.application.Application(urls, globals())
        response = app.request(url='/1234', method='POST', data='{}')
        self.assertEqual(response.status, '201 Created')
        self.assertEqual(response.data, '{}')

    def test_application_handles_invalid_urls(self):
        app = rest.application.Application(urls, globals())
        response = app.request(url='/TEST')
        self.assertEqual(response.status, '404 Not Found')

    def test_application_handles_invalid_methods(self):
        app = rest.application.Application(urls, globals())
        response = app.request(method='TEST')
        self.assertEqual(response.status, '405 Method Not Allowed')
