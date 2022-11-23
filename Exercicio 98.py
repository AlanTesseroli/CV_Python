import time
def contador(a, b, c):
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if a < b:
        cont = a
        while cont < b:
            print(f'{cont}',end=' ')
            time.sleep(0.5)
            cont += c
    else:
        cont = a
        while cont >= b:
            print(f'{cont}', end=' ')
            time.sleep(0.5)
            cont -= c

contador(1,10,1)
contador(10,0,2)

print('Agora é a sua vez!')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passe: '))

contador(a,b,c)