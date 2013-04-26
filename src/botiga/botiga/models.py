# -*- coding: utf-8 -*-

from pyramid.security import (
    Allow,
    Everyone,
    )
    
    
class RootFactory(object):
    __acl__ = [ (Allow, Everyone, 'public'),
                (Allow, 'group:registrats', 'registrar'),
                (Allow, 'group:admins', 'admin')
            ]
    def __init__(self, request):
        pass
        

