def vogal(palavra):
    vogais = 'aeiou'
    contador = 0

    for i in palavra.lower():
        if i in vogais:
            contador += 1
    return contador

print(vogal('Palavra'))
