# Primer Parcial Algoritmos y Estructuras de Datos

# 1. Desarrollar una función recursiva que permita listar los elementos de vector/lista de
# manera inversa al que están cargados. Preferentemente la función solo debe tener un
# parámetro que es la lista de elementos. 

def listarinversa(lista):
    if len(lista) == 0:
        return []
    else:
        return listarinversa(lista[1:]) + [lista[0]]


mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
lista_inversa = listarinversa(mi_lista)
print(lista_inversa) 





