from webob import Request

req = Request.blank('post')
req.host = 'httpbin.org'
req.method = 'POST'
req.content_type = 'application/x-www-form-urlencoded'
req.body = 'firstname=Nick&lastname=Vernal&group=2&message=lal&'.encode()
req.content_length = len(req.body)
req.environ['SERVER_NAME'] = 'httpbin.org'
req.headers['Connection'] = 'close'

resp = req.get_response()
resp.content_type = 'text/plain'
resp.charset = 'utf-8'
print(resp)