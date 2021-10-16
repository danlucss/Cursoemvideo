'''Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104,
 incluindo agora a possibilidade da digitação de um número de tipo inválido.
 Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''

import numeros

a = numeros.leiaInt('Digite um número inteiro: ')
b = numeros.leiaReal('Digite um número real: ')
print(f'O úsuario digiou o numero inteiro {a} e o numero real {b}.')
