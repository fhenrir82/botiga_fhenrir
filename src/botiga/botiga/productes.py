import os
here = os.path.dirname(os.path.abspath(__file__))

def Productes():
    diccionari={}
    fitxer=here+'/objectes.txt'
    prods = open(fitxer,'r')
    for linia in prods:
        linia=linia.rstrip()
        id,producte,unitats,preu=linia.split(',')
        diccionari.update({id:{'producte':producte, 'unitats':unitats, 'preu':preu}})
    prods.close()
    return diccionari
