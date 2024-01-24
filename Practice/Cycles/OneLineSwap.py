#JhonmaSG

#Data sorting cycles
#One Line Swapping using in interview for Junior Programmer

#En una lista con n elementos, se debe aplicar un reverso a los elementos de la lista, donde el ultimo elemento de la lista sea el primero, el segundo como el penultimo y asi sucesivamente.
#No se puede usar funciones reconstruidas

def reverse_list(lista):
    inicio = 0
    #Leg(longitud de la lista) menos 1
    fin = len(lista) -1
    while inicio < fin:
        lista[inicio], lista[fin] = lista[fin], lista[inicio] #One Line Swapping

        inicio += 1
        fin -= 1
    return lista

lista_original =  [1, 2, 3, 4, 5, 6, 7, 8]
print(lista_original)
print(reverse_list(lista_original))