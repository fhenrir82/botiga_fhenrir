import os
here = os.path.dirname(os.path.abspath(__file__))
from pyramid.interfaces import IDict

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
    
def Guardar(request,usuari):
	diccionari=Productes()
	num=NumComanda()
	llista=[]
	fitxer=here+'/comanda.txt'
	comanda=open(fitxer,'a')
	for key in request.POST.keys():
		quantitat=request.POST[key]
		if (quantitat != "acceptar"):
			if quantitat.isdigit():
				if quantitat != "0":
					preu,producte,unitats=diccionari[key]
					comanda.write("usuari:"+usuari+"/ NumComanda:"+str(num)+"/ Idproducte:"+key+"/ producte:"+diccionari[key][producte]+"/ unitats:"+diccionari[key][unitats]+"/ quantitat:"+quantitat+"/ preu:"+diccionari[key][preu]+"\n")
					total=float(diccionari[key][preu])*float(quantitat)
					total="{0:.2f}".format(total)
					llista.append([num,key,diccionari[key][producte],diccionari[key][unitats],quantitat,diccionari[key][preu],total])
	comanda.close()
	return llista

def NumComanda():
	fitxer=here+'/numeracio.txt'
	cmd = open(fitxer,'r')
	for linia in cmd:
		linia=linia.rstrip()
	num=int(linia)
	cmd.close()
	cmd= open(fitxer,'w+')
	linia=int(linia)+1
	cmd.write(str(linia))
	cmd.close()
	return linia

def RetComanda():
	diccionari={}
	llista=[]
	fitxer=here+'/comanda.txt'
	cmd = open(fitxer,'r')
	for linia in cmd:
		if linia !='':
			linia=linia.rstrip()
			llista=linia.split('/')
			tmp,usuari=llista[0].split(':')
			tmp,numcomanda=llista[1].split(':')
			tmp,idprod=llista[2].split(':')
			tmp,producte=llista[3].split(':')
			tmp,unitats=llista[4].split(':')
			tmp,quantitat=llista[5].split(':')
			tmp,preu=llista[6].split(':')
			diccionari.update({numcomanda:{'idprod':idprod,'producte':producte, 'unitats':unitats,'quantitat':quantitat, 'preu':preu}})
			#numcomanda,idprod,producte,unitats,quantitat,preu=linia.split('/ ')
		#diccionari.update({numcomanda:{'idprod':idprod,'producte':producte, 'unitats':unitats,'quantitat':quantitat, 'preu':preu}})
		#print diccionari
	cmd.close()
	
	return diccionari
	
#RetComanda()
