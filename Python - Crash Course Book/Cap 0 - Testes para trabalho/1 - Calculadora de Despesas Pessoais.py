despesas = []

class Despesa():
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

def adicionar_despesas():
    while True:
        nome = str(input('Nome do item: '))
        if not nome:
            print('Algo deu errado, tente novamente!')
        else:
            break
    while True:
        valor = float(input('Valor: R$ '))
        if valor == str:
            print('Digite apenas numeros, tente novamente!')
        else:
            break
    despesa = Despesa(nome, valor)
    despesas.append(despesa)
    print('Dispesa adicionada com sucesso!')

def lista_despesas():
    print('Lista de despesas')
    for i, despesa in enumerate(despesas, 1):
        print(f'{i} - {despesa.nome} --> R$ {despesa.valor}')

def soma_despesas():
    print('Soma das despesas')
    total = sum(despesa.valor for despesa in despesas)
    print(f'TOTAL --> R$ {total}')

while True:
    print('CALCULADORA DE DESPESAS')
    print('Opções: ')
    print('1. Adicionar despesa')
    print('2. Listas despesas')
    print('3. Calcula soma de despesas')
    print('4. Sair')


    opcao = input('Selecione: ')

    if int(opcao) == 1:
        adicionar_despesas()
    elif int(opcao) == 2:
        lista_despesas()

    elif int(opcao) == 3:
        soma_despesas()

    elif int(opcao) == 4:
        print('Certo, até mais!')
        break

    else:
        print('Tente novamente, o valor não foi aceito')