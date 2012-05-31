import werkzeug as werk
from werkzeug.serving import run_simple
import rest.response


class Application(object):
    """This class is the basis for all rest.py applications.

    This class will consume a dictionary of URL routes and a dictionary of the
    scope in which the URL routes are defined.

    URL routes are converted to werkzeug routes then a standard WSGI application
    interface is exposed.
    """

    def __init__(self, urls, globs):
        self.urls = urls
        self.globs = globs

        self._parse_urls()

    def _parse_urls(self):
        """This function converts a dictionary of routes into werkzeug routes."""

        urls = self.urls
        self.urls = werk.routing.Map()

        for key, value in urls.iteritems():
            self.urls.add(werk.routing.Rule(key, endpoint=value))

    def request(self, url='/', method='GET', data=None):
        """This function simulates a request and returns a Response object.

        This function accepts three parameters:

        1.  url

            The url property is the target route to request. Ex: '/Customer'

        2.  method

            The method property is the target HTTP verb to use. Ex: 'POST'

        3.  data

            The data property is any request body data that needs to be sent
            to the target url.
        """

        env = werk.EnvironBuilder(path=url, method=method, data=data)
        env = env.get_environ()

        request = werk.Request(env)
        urls = self.urls.bind_to_environ(env)
        try:
            endpoint, args = urls.match()
        except werk.exceptions.HTTPException:
            return rest.response.not_found()

        if isinstance(endpoint, Application):
            r, a = urls.match(return_rule=True)
            print r
            return endpoint.request(url=url, method=method, data=data)

        if type(endpoint) in [str, unicode]:
            if endpoint not in self.globs:
                return rest.response.not_found()

            target = self.globs[endpoint]()

            if hasattr(target, request.method) is not True:
                return rest.response.method_not_allowed()
        args['request'] = request
        response = getattr(target, request.method)(**args)

        return response

    def __call__(self, environ, start_response):
        """This function provides the Application object with a WSGI interface.

        Unlike the `request` function, this function will execute the WSGI
        application and return a WSGI compatible iterator.
        """

        request = werk.Request(environ)

        urls = self.urls.bind_to_environ(environ)
        try:
            endpoint, args = urls.match()
        except werk.exceptions.HTTPException:
            return rest.response.not_found()(environ, start_response)

        if isinstance(endpoint, Application):
            return endpoint(environ, start_response)

        if type(endpoint) in [str, unicode]:
            if endpoint not in self.globs:
                return rest.response.not_found()(environ, start_response)

            target = self.globs[endpoint]()

            if hasattr(target, request.method) is not True:
                return rest.response.method_not_allowed()(environ, start_response)
        args['request'] = request
        response = getattr(target, request.method)(**args)

        return response(environ, start_response)

    def run(self, port=8080):
        """This function starts a development server on localhost.

        The server will listen on the provided port number which defaults to
        8080.
        """

        run_simple('localhost', port, self)
