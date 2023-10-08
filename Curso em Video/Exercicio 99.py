import time

def maior(*x):
    cont = maior = 0
    for valor in x:
        print(f'{valor} ',end=' ')
        time.sleep(0.2)
        if cont == 0:
            maior = valor
        else:
            if maior > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor foi {maior}')


maior(0,1,2,3,4,5,6)
maior(4,7,0)
maior(1, 2)
maior(6)
maior()
