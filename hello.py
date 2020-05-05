def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [bytes('a=1\n', 'ascii'), bytes('a=2\n', 'ascii'), bytes('b=3\n', 'ascii') , bytes('Hello!!! \n', 'ascii')]
    #return [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    #return [bytes('\r\n'.join(environ['QUERY_STRING'].split('&')),
    #              encoding="utf8")]
    
