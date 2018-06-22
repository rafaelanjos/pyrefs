import unittest
from calculadora import Calculadora

class CalculadoraTest(unittest.TestCase):

    def test_soma(self):
        value = Calculadora.soma(1,1)
        self.assertEqual(2, value)

    def test_sub(self):
        value = Calculadora.subtrair(1,1)
        self.assertEqual(0, value)

    def test_divisao(self):
        value = Calculadora.dividir(10,2)
        self.assertEqual(5, value,"Houve problemas ao tentar dividir")

if __name__ == "__main__":
    unittest.main()