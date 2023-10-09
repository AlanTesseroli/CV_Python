class Cadastro():
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def nome_completo(self, primeironome, nomedomeio, sobrenome):
        if nomedomeio == '1':
            self.nomecompleto = primeironome + ' ' + sobrenome
        else:
            self.nomecompleto = primeironome + ' ' + nomedomeio + ' ' + sobrenome
        return self.nomecompleto

    def cadastro_sucesso(self, nome, idade, email):
        print(f'Olá, {nome}, ficamos muito felizes que uma pessoa com {idade} anos realizou um cadastro, o email cadastrado foi {email}')

first_name = str(input('Qual seu primeiro nome? '))
print('Se não possuir nome do meio, digite 1 ')
mid_name = str(input('Qual seu nome do meio? (opcional) '))
last_name = str(input('Qual seu sobrenome: '))
age = int(input('Qual sua idade: '))
mail =str(input('Qual seu email: '))

cliente = Cadastro(last_name, age, mail)
nomecompleto = cliente.nome_completo(first_name,mid_name,last_name)
cliente.cadastro_sucesso(nomecompleto,age,mail)