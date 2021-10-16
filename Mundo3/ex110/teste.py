'''
Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro()
 e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
 '''

import moeda

p = float(input('Digite um preço: R$'))

moeda.resumo(p, 20, 10)
