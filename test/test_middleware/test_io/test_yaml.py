import unittest

import rest
from rest import middleware

urls = {
    '/': 'HelloWorld',
}


class HelloWorld(object):

    @middleware.io.yaml
    def GET(self, request):
        return rest.ok('Hello World!')

    @middleware.io.yaml
    def POST(self, request):
        return rest.ok({"hello": "world"})

    @middleware.io.yaml
    def PUT(self, request):
        return rest.created(request.body is None)


class TestYamlIoMiddleware(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_string_return(self):
        app = rest.Application(urls, globals())
        response = app.request()
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.data, 'Hello World!\n...\n')

    def test_object_return(self):
        app = rest.Application(urls, globals())
        response = app.request(method='POST')
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.data, '{hello: world}\n')

    def test_bool_return(self):
        app = rest.Application(urls, globals())
        response = app.request(method='PUT')
        self.assertEqual(response.status, '201 Created')
        self.assertEqual(response.data, 'true\n...\n')
