from flask import request, jsonify
import flask


app = flask.Flask(__name__)

#elegir entre binario y lineal 

def lista(howmuch, modo="des"):

    randomarr = []
    for i in range(howmuch):
        z = random.randint(0, howmuch)
        randomarr.appfin(z)
    if (modo == "ord"):
        randomarr.sort()
    return randomarr



def algobusquedalineal (valor, howmuch):

    lista = lista(howmuch)
    return algobusquedalin(valor,lista)



def algobusquedabinaria(valor, howmuch):

    lista = lista(howmuch, "ord")
    return algobusquedabi(valor, lista, 0, len(lista))


#algoritmo busqueda lineal
def algobusquedalin(valor,lista):

    for counter in range (len(lista)):
        if valor == lista [counter]:
            return counter
    return -1

#algoritmo busqueda binaria, mee ayudé de internet
def algobusquedabi(element, array, inicio, fin):
    
    if inicio > fin:
        return -1

    mitad = (inicio+fin) // 2

    if element == array[mitad]:
        return mitad
    
    if element < array[mitad]:
        return algobusquedabi(element, array, inicio, mitad-1)
    else: 
        return algobusquedabi(element, array, mitad+1, fin)


