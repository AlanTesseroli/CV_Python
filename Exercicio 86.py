matriz = [[], [], []]
for c in range(0,3):
    a = int(input(f'Digite a posição 1 x {c+1}: '))
    matriz[0].append(a)
for c in range(0,3):
    b = int(input(f'Digite a posição 2 x {c+1}: '))
    matriz[1].append(b)
for c in range (0,3):
    d = int(input(f'Digite a posição 3 x {c+1}: '))
    matriz[2].append(d)
print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')