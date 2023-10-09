import json

arquivo = 'usuario.json'
try:
    with open(arquivo) as f_obj:
        usuario = json.load(f_obj)
except FileNotFoundError:
    usuario = str(input('Qual seu nome: '))
    with open(arquivo, 'w') as f_obj:
        json.dump(usuario, f_obj)
        print(f'Certo, {usuario}, vou me lembrar de você na próxima vez')
else:
    print(f'Seja bem vindo novamente, {usuario}')
