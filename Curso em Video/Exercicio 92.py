pessoa = {}
nome = {'Nome': str(input('Digite o nome: '))}
pessoa.update(nome)
nascimento = int(input('Digite o ano do seu nascimento: '))
nasc = {'Idade': 2022-nascimento}
pessoa.update(nasc)
ctps = {'CTPS': int(input('Carteira de trabalho (0 não tem): '))}
pessoa.update(ctps)
if pessoa['CTPS'] == 0:
    print('-=-'*30)
else:
    contratação = {'Ano de contratação': int(input('Digite o ano da sua contratação: '))}
    pessoa.update(contratação)
    salario = {'Salário': float(input('Digite seu salário: R$ '))}
    pessoa.update(salario)
    apos = (pessoa['Ano de contratação'] - nascimento) + 35
    aposentadoria = {'Aposentadoria': apos}
    pessoa.update(aposentadoria)
for c, i in pessoa.items():
    print(f'{c} tem o valor {i}')
