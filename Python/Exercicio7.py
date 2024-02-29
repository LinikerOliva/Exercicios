def intersecao(lista1, lista2):
    elementos_comuns = []
    for item1 in lista1:
        if item1 in lista2 and item1 not in elementos_comuns:
            elementos_comuns.append(item1)

    return elementos_comuns

lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]

resultado = intersecao(lista1, lista2)
print("Interseção das listas:", resultado)
