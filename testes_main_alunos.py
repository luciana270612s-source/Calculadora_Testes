import unittest
import math

from main import calculadora, calculadora_v2, calculadora_v3, calculadora_v4


class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.funcoes = [
            calculadora,
            calculadora_v2,
            calculadora_v3,
            calculadora_v4
        ]

    def verificar_nan(self, resultado):
        self.assertTrue(math.isnan(resultado))

    def test_operacoes_basicas_soma(self):
        for funcao in self.funcoes:
            self.assertEqual(funcao(2, 3, '+'), 5)

    def test_operacoes_basicas_subtracao(self):
        for funcao in self.funcoes:
            self.assertEqual(funcao(5, 2, '-'), 3)

    def test_operacoes_basicas_multiplicacao(self):
        for funcao in self.funcoes:
            self.assertEqual(funcao(4, 3, '*'), 12)

    def test_operacoes_basicas_divisao(self):
        for funcao in self.funcoes:
            self.assertEqual(funcao(10, 2, '/'), 5)

    def test_operacoes_basicas_modulo(self):
        for funcao in self.funcoes:
            self.assertEqual(funcao(10, 3, '%'), 1)

    def test_operacoes_basicas_exponenciacao(self):
        for funcao in self.funcoes:
            self.assertEqual(funcao(2, 3, '^'), 8)

    def test_divisao_por_zero(self):
        for funcao in self.funcoes:
            self.verificar_nan(funcao(5, 0, '/'))

    def test_modulo_por_zero(self):
        for funcao in self.funcoes:
            self.verificar_nan(funcao(5, 0, '%'))

    def test_operador_invalido_cifrao(self):
        for funcao in self.funcoes:
            self.verificar_nan(funcao(2, 3, '$'))

    def test_operador_invalido_cardinal(self):
        for funcao in self.funcoes:
            self.verificar_nan(funcao(2, 5, '#'))

    def test_operador_invalido_texto(self):
        for funcao in self.funcoes:
            self.verificar_nan(funcao(0, 2, 'qwe'))

    def test_numeros_float_soma(self):
        for funcao in self.funcoes:
            self.assertAlmostEqual(funcao(2.5, 1.5, '+'), 4.0)

    def test_numeros_float_subtracao(self):
        for funcao in self.funcoes:
            self.assertAlmostEqual(funcao(4.5, 1.5, '-'), 3.0)

    def test_numeros_float_multiplicacao(self):
        for funcao in self.funcoes:
            self.assertAlmostEqual(funcao(5.5, 1.5, '*'), 8.25)

    def test_numeros_float_divisao(self):
        for funcao in self.funcoes:
            self.assertAlmostEqual(funcao(7.5, 2.5, '/'), 3.0)

    def test_numeros_negativos_soma(self):
        for funcao in self.funcoes:
            self.assertEqual(funcao(-2, 3, '+'), 1)

    def test_numeros_negativos_subtracao(self):
        for funcao in self.funcoes:
            self.assertEqual(funcao(-2, 3, '-'), -5)

    def test_numeros_negativos_multiplicacao(self):
        for funcao in self.funcoes:
            self.assertEqual(funcao(-2, 3, '*'), -6)

    def test_numeros_negativos_divisao(self):
        for funcao in self.funcoes:
            self.assertEqual(funcao(-6, 3, '/'), -2.0)

    def test_numeros_negativos_modulo(self):
        for funcao in self.funcoes:
            self.assertEqual(funcao(-7, 3, '%'), 2)

    def test_numeros_negativos_exponenciacao(self):
        for funcao in self.funcoes:
            self.assertEqual(funcao(-2, 3, '^'), -8)

    def test_zero_no_primeiro_numero_com_soma(self):
        for funcao in self.funcoes:
            self.assertEqual(funcao(0, 3, '+'), 3)

    def test_zero_no_primeiro_numero_com_subtracao(self):
        for funcao in self.funcoes:
            self.assertEqual(funcao(0, 3, '-'), -3)

    def test_zero_no_primeiro_numero_com_multiplicacao(self):
        for funcao in self.funcoes:
            self.assertEqual(funcao(0, 3, '*'), 0)

    def test_zero_no_primeiro_numero_com_divisao(self):
        for funcao in self.funcoes:
            self.assertEqual(funcao(0, 3, '/'), 0)

    def test_zero_no_primeiro_numero_com_modulo(self):
        for funcao in self.funcoes:
            self.assertEqual(funcao(0, 3, '%'), 0)

    def test_zero_no_primeiro_numero_com_exponenciacao(self):
        for funcao in self.funcoes:
            self.assertEqual(funcao(0, 3, '^'), 0)


if __name__ == '__main__':
    unittest.main()