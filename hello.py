def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [bytes('a=1\n', 'a=2\n', 'b=3\n', 'ascii')]
    #return [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    #return [bytes('\r\n'.join(environ['QUERY_STRING'].split('&')),
    #              encoding="utf8")]
