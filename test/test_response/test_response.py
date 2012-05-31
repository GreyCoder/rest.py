import unittest
import rest.response


class TestRestApplication(unittest.TestCase):

    def test_setUp(self):
        pass

    def test_tearDown(self):
        pass

    def test_ok(self):
        r = rest.response.ok()
        self.assertEqual(r.status, '200 OK')

    def test_created(self):
        r = rest.response.created()
        self.assertEqual(r.status, '201 Created')

    def test_accepted(self):
        r = rest.response.accepted()
        self.assertEqual(r.status, '202 Accepted')

    def test_non_authoritative_information(self):
        r = rest.response.non_authoritative_information()
        self.assertEqual(r.status, '203 Non-Authoritative Information')

    def test_no_content(self):
        r = rest.response.no_content()
        self.assertEqual(r.status, '204 No Content')

    def test_reset_content(self):
        r = rest.response.reset_content()
        self.assertEqual(r.status, '205 Reset Content')

    def test_partial_content(self):
        r = rest.response.partial_content()
        self.assertEqual(r.status, '206 Partial Content')

    def test_multiple_choices(self):
        r = rest.response.multiple_choices()
        self.assertEqual(r.status, '300 Multiple Choices')

    def test_moved_permanently(self):
        r = rest.response.moved_permanently()
        self.assertEqual(r.status, '301 Moved Permanently')

    def test_found(self):
        r = rest.response.found()
        self.assertEqual(r.status, '302 Found')

    def test_see_other(self):
        r = rest.response.see_other()
        self.assertEqual(r.status, '303 See Other')

    def test_not_modified(self):
        r = rest.response.not_modified()
        self.assertEqual(r.status, '304 Not Modified')

    def test_temporary_redirect(self):
        r = rest.response.temporary_redirect()
        self.assertEqual(r.status, '307 Temporary Redirect')

    def test_bad_request(self):
        r = rest.response.bad_request()
        self.assertEqual(r.status, '400 Bad Request')

    def test_unauthorized(self):
        r = rest.response.unauthorized()
        self.assertEqual(r.status, '401 Unauthorized')

    def test_forbidden(self):
        r = rest.response.forbidden()
        self.assertEqual(r.status, '403 Forbidden')

    def test_not_found(self):
        r = rest.response.not_found()
        self.assertEqual(r.status, '404 Not Found')

    def test_method_not_allowed(self):
        r = rest.response.method_not_allowed()
        self.assertEqual(r.status, '405 Method Not Allowed')

    def test_not_acceptable(self):
        r = rest.response.not_acceptable()
        self.assertEqual(r.status, '406 Not Acceptable')

    def test_proxy_authentication_required(self):
        r = rest.response.proxy_authentication_required()
        self.assertEqual(r.status, '407 Proxy Authentication Required')

    def test_request_timeout(self):
        r = rest.response.request_timeout()
        self.assertEqual(r.status, '408 Request Timeout')

    def test_conflict(self):
        r = rest.response.conflict()
        self.assertEqual(r.status, '409 Conflict')

    def test_gone(self):
        r = rest.response.gone()
        self.assertEqual(r.status, '410 Gone')

    def test_length_required(self):
        r = rest.response.length_required()
        self.assertEqual(r.status, '411 Length Required')

    def test_precondition_failed(self):
        r = rest.response.precondition_failed()
        self.assertEqual(r.status, '412 Precondition Failed')

    def test_request_entity_too_large(self):
        r = rest.response.request_entity_too_large()
        self.assertEqual(r.status, '413 Request Entity Too Large')

    def test_request_uri_too_long(self):
        r = rest.response.request_uri_too_long()
        self.assertEqual(r.status, '414 Request-URI Too Long')

    def test_unsupported_media_type(self):
        r = rest.response.unsupported_media_type()
        self.assertEqual(r.status, '415 Unsupported Media Type')

    def test_requested_range_not_satisfiable(self):
        r = rest.response.requested_range_not_satisfiable()
        self.assertEqual(r.status, '416 Requested Range Not Satisfiable')

    def test_expectation_failed(self):
        r = rest.response.expectation_failed()
        self.assertEqual(r.status, '417 Expectation Failed')

    def test_internal_server_error(self):
        r = rest.response.internal_server_error()
        self.assertEqual(r.status, '500 Internal Server Error')

    def test_not_implemented(self):
        r = rest.response.not_implemented()
        self.assertEqual(r.status, '501 Not Implemented')
