import justpy as jp
from api import Api
from documentation import Documentation

jp.JpRoute(Api.path, Api.serve)
jp.JpRoute(Documentation.path, Documentation.serve)
jp.justpy()
