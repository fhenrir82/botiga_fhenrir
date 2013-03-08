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
    
def Dades():
	diccionari={}
	fitxer=here+'/comanda.txt'
	comanda=open(fitxer,'a')
	for linia in comanda:
		fitxer.write('01')
		fitxer.write(' ')
		fitxer.write(llista_valors[0])
		fitxer.write(' ')
		fitxer.write(llista_valors[1])
		fitxer.write('\n')
	
