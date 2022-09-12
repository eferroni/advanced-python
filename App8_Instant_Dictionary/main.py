import justpy as jp

from webapp.home import Home
from webapp.about import About
from webapp.dictionary import Dictionary

jp.JpRoute(Home.path, Home.serve)
jp.JpRoute(About.path, About.serve)
jp.JpRoute(Dictionary.path, Dictionary.serve)

jp.justpy(port=8001)
