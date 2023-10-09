import json

def leitura_usuario():
    """Serve para ler o nome do usuário"""
    usernumber = 'usernumber.json'
    try:
        with open(usernumber) as f_obj:
            numero = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return numero

def cadastro_numero():
    """"Serve para cadastrar um numero quando não houver"""
    numero = int(input('Qual seu numero favorito: '))
    usernumber = 'usernumber.json'
    with open(usernumber, 'w') as f_obj:
        json.dump(numero, f_obj)
    return numero

def numero_favorito():
    """Mensagem para mostrar o numero favorito"""
    try:
        numero = leitura_usuario()
        if numero:
            print(f'Seu numero favorito é {numero}')
    except FileNotFoundError:
        pass
    else:
        numero = cadastro_numero()
        print(f'Certo, vou me lembrar que seu número favorito é {numero}')

def verificacao_usuario():
    numero = leitura_usuario()
    if numero:
        print('------ VERIFICAÇÃO -------')
        verificacao = int(input(f'Qual seu numero favorito: '))
        if verificacao == numero:
            print(f'Bem vindo novamente, seu numero favorito é {verificacao}')
        else:
            cadastro_numero()
    else:
        numero_favorito()

verificacao_usuario()