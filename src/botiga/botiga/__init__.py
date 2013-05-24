# -*- coding: utf-8 -*-
import os
import logging

from pyramid.config import Configurator

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from .security import groupfinder
from .models import RootFactory

from pyramid.events import NewRequest
from pyramid.events import subscriber
from pyramid.events import ApplicationCreated
from pyramid.httpexceptions import HTTPFound
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from pyramid.view import view_config
logging.basicConfig()
log = logging.getLogger(__file__)

here = os.path.dirname(os.path.abspath(__file__))

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    
    #settings['mako.directories'] = os.path.join(here, 'templates')
    settings['mako.directories'] = os.path.join(here, 'templates')
    authn_policy = AuthTktAuthenticationPolicy('sosecret', callback=groupfinder, hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    config = Configurator(root_factory='.models.RootFactory', settings=settings)

    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)

    #config.add_static_view('static', os.path.join(here, 'static'))
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('benvinguda','/')
    config.add_route('home','/home')
    config.add_route('productes','/productes')
    config.add_route('comanda','/comanda')
    config.add_route('informacio','/informacio')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.scan()
    return config.make_wsgi_app()
