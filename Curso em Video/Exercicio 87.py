lista = [[], [], []]
par = []
for c in range(0,3):
    a = int(input(f'Digite o valor da linha 1 coluna {c+1}: '))
    lista[0].append(a)
    if a % 2 == 0:
        par.append(a)
for c in range(0,3):
    b = int(input(f'Digite o valor da linha 1 coluna {c+1}: '))
    lista[1].append(b)
    if b % 2 == 0:
        par.append(b)
for c in range(0,3):
    d = int(input(f'Digite o valor da linha 1 coluna {c+1}: '))
    lista[2].append(d)
    if d % 2 == 0:
        par.append(d)
print('-=-'*30)
print(f'MATRIZ: ')
print(f'{lista[0]}\n{lista[1]}\n{lista[2]}')
print('-=-'*30)
print(f'A soma dos numeros pares foi: {sum(par)}')
print('-=-'*30)
print(f'A soma dos valores da terceira coluna é: {sum(lista[2])}')
print('-=-'*30)
print(f'O maior valor da segunda linha é: {max(lista[1])}')