# -*- coding: utf-8 -*-
from pyramid.httpexceptions import HTTPFound
from pyramid.interfaces import IDict
from pyramid.view import (
    view_config,
    forbidden_view_config,
)
from pyramid.security import (
    remember,
    forget,
    authenticated_userid,
)
from .security import comprova_usuari

#from productes import Productes
#from productes import Guardar
from productes import *
# from fitxer import funcio

@view_config(route_name='home', renderer='templates/mytemplate.pt', permission='public')
def my_view(request):
    return {'project':'botiga','logged_in':authenticated_userid(request)}
@view_config(route_name='benvinguda', renderer='benvinguts.mako', permission='public')
def benvinguda_view(request):
    missatge = "Aleix's Shop"
    return{"miss":missatge,'pagina':'Benvinguts','logged_in':authenticated_userid(request)}
@view_config(route_name='productes', renderer='productes.mako', permission='registrar')
def productes_view(request):
    pros=Productes()

    return {"products":pros,'pagina':'Realitzi la comanda','logged_in':authenticated_userid(request)} 
@view_config(route_name='comanda', renderer='items.mako', permission='registrar')
def items_view(request):
    comanda= Guardar(request,authenticated_userid(request))
    numcomanda=comanda[0][0]
    return{"ncmd":numcomanda,"cmd":comanda,'pagina':'Comanda:','logged_in':authenticated_userid(request)}  
@view_config(route_name='informacio', renderer='informacio.mako', permission='public')
def informacio_view(request):
    veure=RetComanda()
    print veure
    return{'pagina':'Informacio','llistat':veure,'logged_in':authenticated_userid(request)}


# aquest decorator és per establir la ruta per /login
@view_config( route_name='login', renderer='login.mako')
# aquest altre ens redirigirà aquí quan algú intenti entrar en una web que no té permís
@forbidden_view_config(renderer='login.mako')
def login(request):
    login_url = request.route_url('login')
    # detectem des de quina URL ve el visitant
    referrer = request.url
    # retornem l'usuari a la home page si ha vingut directe al login
    if referrer == login_url:
        referrer = '/' # never use the login form itself as came_from
    came_from = request.params.get('came_from', referrer)
    user = authenticated_userid(request)
    if user:
        lloc = came_from.split("/")
        message = "Ets %s, i com a tal no pots entrar a %s" % (user,lloc[len(lloc)-1])
    else:
        message = "Identifica't per entrar a la Botiga"
    login = ''
    password = ''
    if 'form.submitted' in request.params:
        login = request.params['login']
        password = request.params['password']
        if comprova_usuari(login,password):
            headers = remember(request, login)
            return HTTPFound(location = came_from,
                             headers = headers)
        message = 'Failed login'

    return dict(
        message = message,
        url = request.application_url + '/login',
        came_from = came_from,
        login = login,
        password = password,
        user = authenticated_userid(request), # afegim usuari autenticat si l'hi ha
        pagina='Realitzi la comanda')
    
    

@view_config(route_name='logout')
def logout(request):
    headers = forget(request)
    return HTTPFound(location = request.route_url('benvinguda'),
                     headers = headers)
