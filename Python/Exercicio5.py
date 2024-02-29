def maiores_numeros(numeros, q_numeros):
    numeros.sort();
    n = []
    contador = 1;
    while(q_numeros >= contador):
        n.append(numeros[-contador])
        contador += 1
        
    return n

print(maiores_numeros([1,2,3,4,5,6,7,8,9,10,11], 3))