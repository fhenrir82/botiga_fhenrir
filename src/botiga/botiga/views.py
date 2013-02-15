# -*- coding: utf-8 -*-
from pyramid.view import view_config
from productes import Productes
# from fitxer import funcio

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project':'botiga'}

@view_config(route_name='benvinguda', renderer='benvinguts.mako')
def benvinguda_view(request):
    missatge = "Aleix's Shop"
    return{"miss":missatge}
@view_config(route_name='productes', renderer='productes.mako')
def productes_view(request):
    pros=Productes()
    return {"products":pros}
   # aqui aniriem als arxius o la base de dades a buscar la informació
   # així ho simulem, manera alternativa cutre
   #proj = "Botigueta Pro"
   #prod = [ 'pepino' , 'enciam' , 'plàtan' ]
   #preus = { 'pepino':'2€/kg', 'enciam':'1€/peça', 'plàtan':'2.5€/kg' }
   # els retornarem amb:
   #return { "projecte":proj, "productes":prod, "preus":preus }
