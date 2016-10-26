from webob import Request

requests = []


def create_req(get, host='httpbin.org', accept='*/*'):
    req = Request.blank(get)
    req.host = host
    req.environ['SERVER_NAME'] = host
    req.accept = accept
    req.headers['Connection'] = 'close'
    return req

requests.append(create_req('/ip'))
requests.append(create_req('/get?foo=bar&1=2&2/0&error=True'))

req3 = create_req('post')
req3.method = 'POST'
req3.content_type = 'application/x-www-form-urlencoded'
req3.body = 'foo=bar&1=2&2%2F0=&error=True'.encode('utf-8')
req3.content_length = len(req3.body)
requests.append(req3)

requests.append(create_req('/cookies/set?country=Ru'))
requests.append(create_req('/cookies'))
requests.append(create_req('/redirect/4'))

for req in requests:
    resp = req.get_response()
    resp.content_type = 'text/plain'
    resp.charset = 'utf-8'
    print(resp)
    print('\n\n***\n\n')