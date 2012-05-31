import json as jslib
import datetime

from rest import response


def json(f):

    def json_serialize(obj):

        def default(o):
            if isinstance(o, datetime.datetime):
                return str(o.strftime('%Y-%m-%d %H:%M:%S'))

        return jslib.dumps(obj, default=default)

    def json_deserialize(obj):

        return jslib.loads(obj)

    def wrapped(*args, **kwargs):

        req = kwargs.get('request')
        try:
            req.body = json_deserialize(req.body)
        except:
            # If req.body is not empty or None, it is bad JSON.
            if req.body:
                return response.bad_request()

        res = f(*args, **kwargs)
        res.data = json_serialize(res.response[0])
        res.headers.pop('Content-Type', None)
        res.headers.add('Content-Type', 'application/json')

        return res

    return wrapped
