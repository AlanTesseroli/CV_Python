aluno = {}
aluno['Nome'] = str(input('Digite o nome: '))
aluno['Media'] = float(input('Digite a média: '))

for k,v in aluno.items():
    print(f'{k} é igual a {v}')
if aluno['Media'] >= 7:
    print('Aprovado')
elif aluno['Media'] <= 5:
    print('Reprovado')
else:
    print('Recuperação')