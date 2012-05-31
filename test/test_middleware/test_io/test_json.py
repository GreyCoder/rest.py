import unittest

import rest
from rest import middleware

urls = {
    '/': 'HelloWorld',
}


class HelloWorld(object):

    @middleware.io.json
    def GET(self, request):
        return rest.ok('Hello World!')

    @middleware.io.json
    def POST(self, request):
        return rest.ok({"hello": "world"})

    @middleware.io.json
    def PUT(self, request):
        return rest.created(request.body is None)


class TestJsonIoMiddleware(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_string_return(self):
        app = rest.Application(urls, globals())
        response = app.request()
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.data, '"Hello World!"')

    def test_object_return(self):
        app = rest.Application(urls, globals())
        response = app.request(method='POST')
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.data, '{"hello": "world"}')

    def test_bool_return(self):
        app = rest.Application(urls, globals())
        response = app.request(method='PUT')
        self.assertEqual(response.status, '201 Created')
        self.assertEqual(response.data, 'true')
