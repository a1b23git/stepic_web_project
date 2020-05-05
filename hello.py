def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ["a=1","b=2"]
    #return [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    #return [bytes('\r\n'.join(environ['QUERY_STRING'].split('&')),
    #              encoding="utf8")]
