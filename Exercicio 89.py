lista = []
cont = 0
while True:
    n = str(input('Digite o nome do aluno: '))
    n1 = float(input('Digite a 1º nota do aluno: '))
    n2 = float(input('Digite a 2º nota do aluno: '))
    media = (n1+n2)/2
    lista.append([n, [n1,n2], media])
    cont += 1
    r1 = str(input('Deseja continuar [S/N]: ')).upper()
    if r1 in 'Nn':
        break
    else:
        print('-=-'*30)
print(f'{"No":<4}{"Nome":<10}{"Media":>8}')
for i, l in enumerate(lista):
    print(f'{i:<4} {l[0]:<10} {l[2]:>8}')
while True:
    print('-'*20)
    x = int(input('Você gostaria de mostrar as notas de qual aluno (999 interrompe): '))
    if x <= cont:
        print(lista[x][1])
    elif x == 999:
        break
    elif x > cont:
        print('Tente novamente')
print('FIM')