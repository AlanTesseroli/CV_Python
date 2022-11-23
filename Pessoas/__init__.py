def menu(a):
    print('-'*30)
    print(f'      {a}')
    print('-'*30)


def cabecalho(msg):
    op = (1,2,3)
    print('1 - Ver pessoas cadastradas\n'
          '2 - Cadastrar nova pessoa\n'
          '3 - Sair do sistema')
    while True:
        try:
            x = int(input(msg))
            if x in op:
                if x == 1:
                    print('-' * 30)
                    print(f'PESSOAS CADASTRADAS')
                    print('-' * 30)
                    break
                if x == 2:
                    print('-' * 30)
                    print(f'CADASTRAR NOVA PESSOA')
                    print('-' * 30)
                    break
                if x == 3:
                    print('-' * 30)
                    print(f'SAIR DO SISTEMA')
                    print('-' * 30)
                    break
            else:
                print(f'O número {x} é inválido, tente novamente')
        except:
            print('Erro, tente novamente')


def menupop(a):
    print('-'*30)
    print(f'      {a}')
    print('-'*30)


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro')
    else:
        cabecalho('Pessoas Cadastradas')
        print(a.read())