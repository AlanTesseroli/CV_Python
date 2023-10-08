lista = [[], []]
for c in range (0,7):
    n = int(input(f'Digite o {c+1}º valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print(f'Os números pares são: {sorted(lista[0])}')
print(f'Os números impares são: {sorted(lista[1])}')