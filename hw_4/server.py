from jinja2 import Environment, FileSystemLoader, Template
from wsgiref.simple_server import make_server

_env = Environment(loader=FileSystemLoader('.'))


def app(env, start_resp):
    start_resp('200 OK', [('Content-Type', 'text/html')])
    path = env['PATH_INFO']

    def get_my_template(link):
        return _env.get_template(path) \
            .render(link=link)\
            .encode('utf-8')

    if 'index.html' in path:
        link = """<a href="/about/aboutme.html">about me</a>"""
    elif 'about/aboutme.html' in path:
        link = """<a href="/index.html">index</a>"""

    return get_my_template(link)

if __name__ == '__main__':
    serv = make_server('', 8000, app)
    serv.serve_forever()