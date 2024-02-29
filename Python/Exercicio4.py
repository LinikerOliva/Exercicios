def contar_ocorrencias(frase, palavra):
    return frase.lower().count(palavra.lower())

print(contar_ocorrencias("Esta é uma frase de exemplo com várias palavras. Contar quantas vezes a palavra 'frase' aparece.", 'frase'))