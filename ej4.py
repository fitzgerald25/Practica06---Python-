def superposicion(lista1,lista2):

	listado1 = lista1.split()
	listado2 = lista2.split()
	resultado = False
	for i in range(0,len(listado1)):
		for x in range(0,len(listado2)):
			if listado1[i]==listado2[x]:
				resultado =  True
	print (resultado)



lista1 = input("dime algo ")
lista2 = input("Dime otra cosa ")
superposicion(lista1, lista2)