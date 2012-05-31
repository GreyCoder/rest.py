import werkzeug as werk


def ok(content='', headers={}):

    return werk.Response(content if hasattr(content, 'next') else [content],
                        headers=headers, status='200 OK')


def created(content='', headers={}):

    return werk.Response(content if hasattr(content, 'next') else [content],
                        headers=headers, status='201 Created')


def accepted(content='', headers={}):

    return werk.Response(content if hasattr(content, 'next') else [content],
                        headers=headers, status='202 Accepted')


def non_authoritative_information(content='', headers={}):

    return werk.Response(content if hasattr(content, 'next') else [content],
                        headers=headers,
                        status='203 Non-Authoritative Information')


def no_content(headers={}):

    return werk.Response('', headers=headers, status='204 No Content')


def reset_content(headers={}):

    return werk.Response('', headers=headers, status='205 Reset Content')


def partial_content(content='', headers={}):

    return werk.Response(content if hasattr(content, 'next') else [content],
                        headers=headers, status='206 Partial Content')


def multiple_choices(content='', headers={}):

    return werk.Response(content if hasattr(content, 'next') else [content],
                        headers=headers,
                        status='300 Multiple Choices')


def moved_permanently(content='', headers={}):

    return werk.Response(content if hasattr(content, 'next') else [content],
                        headers=headers,
                        status='301 Moved Permanently')


def found(content='', headers={}):

    return werk.Response(content if hasattr(content, 'next') else [content],
                        headers=headers, status='302 Found')


def see_other(content='', headers={}):

    return werk.Response(content if hasattr(content, 'next') else [content],
                        headers=headers, status='303 See Other')


def not_modified(content='', headers={}):

    return werk.Response(content if hasattr(content, 'next') else [content],
                        headers=headers, status='304 Not Modified')


def temporary_redirect(content='', headers={}):

    return werk.Response(content if hasattr(content, 'next') else [content],
                        headers=headers,
                        status='307 Temporary Redirect')


def bad_request(content='', headers={}):

    return werk.Response(content if hasattr(content, 'next') else [content],
                        headers=headers, status='400 Bad Request')


def unauthorized(content='', headers={}):

    return werk.Response(content if hasattr(content, 'next') else [content],
                        headers=headers, status='401 Unauthorized')


def forbidden(content='', headers={}):

    return werk.Response(content if hasattr(content, 'next') else [content],
                        headers=headers, status='403 Forbidden')


def not_found(content='', headers={}):

    return werk.Response(content if hasattr(content, 'next') else [content],
                        headers=headers, status='404 Not Found')


def method_not_allowed(content='', headers={}):

    return werk.Response(content if hasattr(content, 'next') else [content],
                        headers=headers,
                        status='405 Method Not Allowed')


def not_acceptable(content='', headers={}):

    return werk.Response(content if hasattr(content, 'next') else [content],
                        headers=headers, status='406 Not Acceptable')


def proxy_authentication_required(content='', headers={}):

    return werk.Response(content if hasattr(content, 'next') else [content],
                        headers=headers,
                        status='407 Proxy Authentication Required')


def request_timeout(content='', headers={}):

    return werk.Response(content if hasattr(content, 'next') else [content],
                        headers=headers, status='408 Request Timeout')


def conflict(content='', headers={}):

    return werk.Response(content if hasattr(content, 'next') else [content],
                        headers=headers, status='409 Conflict')


def gone(content='', headers={}):

    return werk.Response(content if hasattr(content, 'next') else [content],
                        headers=headers, status='410 Gone')


def length_required(content='', headers={}):

    return werk.Response(content if hasattr(content, 'next') else [content],
                        headers=headers, status='411 Length Required')


def precondition_failed(content='', headers={}):

    return werk.Response(content if hasattr(content, 'next') else [content],
                        headers=headers,
                        status='412 Precondition Failed')


def request_entity_too_large(content='', headers={}):

    return werk.Response(content if hasattr(content, 'next') else [content],
                        headers=headers,
                        status='413 Request Entity Too Large')


def request_uri_too_long(content='', headers={}):

    return werk.Response(content if hasattr(content, 'next') else [content],
                        headers=headers,
                        status='414 Request-URI Too Long')


def unsupported_media_type(content='', headers={}):

    return werk.Response(content if hasattr(content, 'next') else [content],
                        headers=headers,
                        status='415 Unsupported Media Type')


def requested_range_not_satisfiable(content='', headers={}):

    return werk.Response(content if hasattr(content, 'next') else [content],
                        headers=headers,
                        status='416 Requested Range Not Satisfiable')


def expectation_failed(content='', headers={}):

    return werk.Response(content if hasattr(content, 'next') else [content],
                        headers=headers,
                        status='417 Expectation Failed')


def internal_server_error(content='', headers={}):

    return werk.Response(content if hasattr(content, 'next') else [content],
                        headers=headers,
                        status='500 Internal Server Error')


def not_implemented(content='', headers={}):

    return werk.Response(content if hasattr(content, 'next') else [content],
                        headers=headers, status='501 Not Implemented')
