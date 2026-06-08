
# test_calculadora.py

import unittest

from calculadora import dividir, multiplicar, somar, subtrair, potencia, calcular_media


class TestCalculadora(unittest.TestCase):
    """Classe de testes para as funções do arquivo calculadora.py."""
    
    def test_media_numeros_inteiros(self):
        self.assertEqual(calcular_media([10, 8, 6]), 8)
        self.assertEqual(calcular_media([5, 5, 5]), 5)

    def test_media_numeros_decimais(self):
        self.assertAlmostEqual(calcular_media([7.5, 8.5, 9.0]), 8.3333, places=3)

    def test_media_com_apenas_um_numero(self):
        self.assertEqual(calcular_media([10]), 10)
        self.assertEqual(calcular_media([4.5]), 4.5)

    def test_media_lista_vazia(self):
        with self.assertRaises(ValueError):
            calcular_media([])
    
    def  test_potencia(self):
        self.assertEqual(potencia(2, 3), 8)
        self.assertEqual(potencia(5, 0), 1)
        self.assertEqual(potencia(10, 2), 100)

    def test_somar(self):
        """Testa se a função somar está funcionando corretamente."""
        self.assertEqual(somar(2, 3), 5)
        self.assertEqual(somar(-1, 1), 0)
        self.assertEqual(somar(0, 0), 0)

    def test_subtrair(self):
        """Testa se a função subtrair está funcionando corretamente."""
        self.assertEqual(subtrair(10, 5), 5)
        self.assertEqual(subtrair(5, 10), -5)
        self.assertEqual(subtrair(0, 0), 0)

    def test_multiplicar(self):
        """Testa se a função multiplicar está funcionando corretamente."""
        self.assertEqual(multiplicar(3, 4), 12)
        self.assertEqual(multiplicar(5, 0), 0)
        self.assertEqual(multiplicar(-2, 3), -6)

    def test_dividir(self):
        """Testa se a função dividir está funcionando corretamente."""
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(9, 3), 3)
        self.assertEqual(dividir(5, 2), 2.5)

    def test_dividir_por_zero(self):
        """Testa se a divisão por zero gera erro."""
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)
    



if __name__ == "__main__":
    unittest.main()
