def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [(i + '\n') for i in environ['QUERY_STRING'].split('&')]
    #return [bytes('\r\n'.join(environ['QUERY_STRING'].split('&')),
    #              encoding="utf8")]
