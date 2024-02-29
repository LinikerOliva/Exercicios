def contador_palavras(texto):
    palavra = texto.split()
    return len(palavra)

print(contador_palavras('as aulas terminaram as dez e quinze da noite'))