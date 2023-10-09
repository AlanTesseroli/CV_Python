import unittest
from city_functions import cidade_pais

class CityTest(unittest.TestCase):
    """Teste para verificação do nome das cidades"""
    def teste_cidade_pais(self):
        formatado = cidade_pais('palmas', 'bRasil','50.000')
        self.assertEqual(formatado, 'Cidade --> Palmas/ País --> Brasil/ População --> 50.000 hab.')
unittest.main()