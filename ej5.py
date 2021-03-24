lista =[]

def CargarLista():
    for x in range(10):
        numero = int(input("ESCRIBA UN NUMERO"))
        lista.append(numero)

def MostrarLista():
    print(lista)


CargarLista()
MostrarLista()