pessoa = {}
todos = []
idadetot = []
mulheres = []
geral = {}
cont = 0

while True:
    pessoa.update({'nome': str(input('Digite o nome: '))})
    pessoa.update({'sexo': str(input('Digite o sexo [M/F]: ')).upper()})
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    pessoa.update({'idade': int(input('Digite a idade: '))})
    todos.append(pessoa.copy())
    idadetot.append(pessoa['idade'])
    cont += 1
    r = str(input('Gostaria de continuar [S/N]: ')).upper()
    if r in 'N':
        break
med = sum(idadetot)/cont
print('-=-'*30)
print(f'Foram cadastradas {len(todos)} pessoas')
print('-=-'*30)
print(f'A média de idade do grupo foi {med} anos')
print('-=-'*30)
print(f'As mulheres são: {mulheres}')
print('-=-'*30)
print(f'As pessoas com idade acima da média são: ')
for c in todos:
    for k, v in c.items():
        if k in 'idade' and v > med:
            print(f'{c}')
            print(' ')
