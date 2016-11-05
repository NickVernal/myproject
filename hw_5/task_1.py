from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from jinja2 import FileSystemLoader, Environment

env = Environment(loader=FileSystemLoader('.'))


def index_page(request):
    return Response(env.get_template('index.html')
                    .render(link="""<a href="/about/aboutme.html">about me</a>"""))


def about_me_page(request):
    return Response(env.get_template('about/aboutme.html')
                    .render(link="""<a href="/index.html">index</a>"""))


if __name__ == '__main__':
    configurator = Configurator()
    configurator.add_view(index_page, route_name='index')
    configurator.add_route('index', '/index.html')
    configurator.add_view(about_me_page, route_name='about_me')
    configurator.add_route('about_me', '/about/aboutme.html')
    app = configurator.make_wsgi_app()
    server = make_server('localhost', 8080, app=app)
    server.serve_forever()
