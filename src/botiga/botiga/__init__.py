# -*- coding: utf-8 -*-
from pyramid.config import Configurator
import os

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    #el here serveix per a poder saber a quina ruta es troba l'arxiu
    settings['mako.directories'] = os.path.join(here, 'templates')
    #amb aquesta linia serveix per no tenir problemes amb els templates
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('benvinguda','/botiga') #productes=view, /botiga=URL
    config.add_route('productes','/botiga/productes')
    config.scan()
    return config.make_wsgi_app()
