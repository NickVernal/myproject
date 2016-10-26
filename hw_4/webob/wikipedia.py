from webob import Request

req = Request.blank('/wiki/Samy_Kamkar')
req.host = 'en.wikipedia.org'
req.user_agent = 'Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.9b5)' +\
    ' Gecko/2008050509 Firefox/3.0b5'
req.accept = 'text/html'
req.environ["SERVER_NAME"] = 'wikipedia.org'

resp = req.get_response()
resp.content_type = 'text/plain'
resp.charset = 'utf-8'
print(resp)
