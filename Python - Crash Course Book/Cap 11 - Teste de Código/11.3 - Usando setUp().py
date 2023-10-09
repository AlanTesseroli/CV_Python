import unittest

class Funcionario():

    def __init__(self, primeiro_nome, sobrenome, salario):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome
        self.salario = salario

    def info(self):
        return f'{self.primeiro_nome} {self.sobrenome} tem o salário de R$ {self.salario},00'

    def aumento(self, bonus=5000):
        self.salario += bonus

alan = Funcionario('Alan', 'Tesseroli', 5000)
alan.aumento()
print(alan.info())

class TesteFuncionario(unittest.TestCase):
    def setUp(self):
        self.funcionario = Funcionario('Alan', 'Tesseroli', 7500)

    def test_give_default_raise(self):
        self.funcionario.aumento()
        self.assertEqual(self.funcionario.salario, 12500)

    def test_give_custom_raise(self):
        self.funcionario.aumento(bonus=10000)
        self.assertEqual(self.funcionario.salario, 17500)

unittest.main()