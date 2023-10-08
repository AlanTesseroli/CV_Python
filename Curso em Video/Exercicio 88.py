import random
import time
lista = []
jogos = []
tot = 1
cont = 0
print('-=-'*30)
print('SORTEIOS MEGA SENA')
print('-=-'*30)
x = int(input('Quantos jogos você gostaria de fazer: '))
print('-=-'*30)
while tot <= x:
    cont = 0
    while True:
        a = random.randint(0,60)
        if a not in lista:
            lista.append(a)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    print('-=-' * 30)
    time.sleep(2)





