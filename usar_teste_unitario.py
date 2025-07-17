# Importar o modulo unittest que nos ermite escrever teste automatizadas
import unittest

#importar as funções de teste
from teste_unitario import somar, subtrair, multiplicar, dividir

#criar a classe que contem os testes unitarios para as funções de operação
class TesteOperacoes(unittest.TestCase):
    #testar a função de soma
    def testar_soma(self):
        # verificar se a soma de 2 e 3 é igual a 5
        self.assertEqual(somar(2,3),5)

        # verificar se a soma de -1 e 1 é igual a 0
        self.assertEqual(somar(-1,1),0)

        # verificar se a soma de -2 e -3 é igual a -5
        self.assertEqual(somar(-2,-3),-5)

    def testar_divisao(self):
        self.assertEqual(dividir(6, 2), 3)
        self.assertEqual(dividir(-6, 3), -2)
        self.assertEqual(dividir(4, 2), 2)
        with self.assertRaises(ValueError):
            dividir(1,0)


    def testar_subtracao(self):
        self.assertEqual(subtrair(8, 3), 5)
        self.assertEqual(subtrair(6, 3), 3)
        self.assertEqual(subtrair(7, 3), 4)

    def testar_multiplicao(self):
        self.assertEqual(multiplicar(3, 3), 9)
        self.assertEqual(multiplicar(2, 3), 6)
        self.assertEqual(multiplicar(2, 2), 4)










#permite que os testes sejam executados quando darmos o arquivo diretamente
if __name__ == '__main__':
    unittest.main() #executa todos os testes definidos na classe
