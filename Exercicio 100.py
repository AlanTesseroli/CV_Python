import random

numeros = list()
def sorteio():
    for c in range (0,5):
        numeros.append(random.randint(0,9))


def somaPar(x):
    cont = 0
    for c in x:
        if c % 2 == 0:
            cont += c
    print(cont)

sorteio()
print(f'Sorteamos 5 valores da lista: {numeros}')
print(f'Somando os valores pares de {numeros}, temos ', end='')
somaPar(numeros)