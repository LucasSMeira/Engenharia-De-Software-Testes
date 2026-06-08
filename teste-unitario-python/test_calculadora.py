
# test_calculadora.py

import unittest

from calculadora import dividir, multiplicar, somar, subtrair, potencia, calcular_media


class TestCalculadora(unittest.TestCase):
    """Classe de testes para as funções do arquivo calculadora.py."""
    
    def test_multiplicar_inteiros_positivos(self):
        """Caso normal: multiplicação de inteiros positivos."""
        self.assertEqual(multiplicar(3, 4), 12)

    def test_multiplicar_por_zero(self):
        """Caso de borda: qualquer número multiplicado por zero resulta em zero."""
        self.assertEqual(multiplicar(7, 0), 0)

    def test_multiplicar_positivo_por_negativo(self):
        """Caso normal: positivo multiplicado por negativo."""
        self.assertEqual(multiplicar(5, -3), -15)

    def test_multiplicar_dois_negativos(self):
        """Caso normal: negativo multiplicado por negativo."""
        self.assertEqual(multiplicar(-4, -6), 24)

    def test_multiplicar_decimais(self):
        """Caso normal: multiplicação com números decimais."""
        self.assertEqual(multiplicar(2.5, 4.0), 10.0)

    def test_multiplicar_por_um(self):
        """Caso de borda: um é o elemento neutro da multiplicação."""
        self.assertEqual(multiplicar(1, 99), 99)

    def test_multiplicar_zero_por_zero(self):
        """Caso de borda: zero multiplicado por zero."""
        self.assertEqual(multiplicar(0, 0), 0)

    def test_multiplicar_entrada_invalida(self):
        """Caso de erro: entrada não numérica deve gerar TypeError."""
        with self.assertRaises(TypeError):
            multiplicar(None, 5)
    
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
    
    def test_potencia(self):
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

    def test_dividir_divisao_exata(self):
        """Caso normal: divisão exata entre inteiros."""
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(9, 3), 3)

    def test_dividir_resultado_decimal(self):
        """Caso normal: divisão com resultado decimal."""
        self.assertEqual(dividir(5, 2), 2.5)

    def test_dividir_numero_negativo(self):
        """Caso normal: dividendo negativo."""
        self.assertEqual(dividir(-10, 2), -5)

    def test_dividir_zero_por_numero(self):
        """Caso de borda: zero dividido por outro número."""
        self.assertEqual(dividir(0, 5), 0)

    def test_dividir_por_zero(self):
        """Caso de erro: divisão por zero deve gerar ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)

    def test_dividir_dois_negativos(self):
        """Caso normal: negativo dividido por negativo."""
        self.assertEqual(dividir(-12, -3), 4)

    def test_dividir_por_um(self):
        """Caso de borda: um é o elemento neutro da divisão."""
        self.assertEqual(dividir(7, 1), 7)

    def test_dividir_zero_por_zero(self):
        """Caso de erro: zero dividido por zero é indefinido."""
        with self.assertRaises(ZeroDivisionError):
            dividir(0, 0)




if __name__ == "__main__":
    unittest.main()
