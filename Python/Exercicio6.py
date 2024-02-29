def somar_matriz(matriz1, matriz2):
    n = len(matriz1)
    m = len(matriz2)
    
    resultado = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            resultado[i][j] = matriz1[i][j] + matriz2[i][j]

    return resultado

matriz1 = [[1, 2, 3], [4, 3, 6], [7, 8, 9]]
matriz2 = [[9, 8, 7], [6, 2, 4], [3, 2, 1]]

print(somar_matriz(matriz1, matriz2))