import random

def embaralhar_lista(lista):
    random.shuffle(lista)
    return lista

minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Lista original:", minha_lista)

lista_embaralhada = embaralhar_lista(minha_lista)
print("Lista embaralhada:", lista_embaralhada)
