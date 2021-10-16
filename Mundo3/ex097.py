"""
Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como
parâmetro e mostre uma mensagem com tamanho adaptável.
"""


def menssagem(msg):
    print('-' * (len(msg) + 4))
    print(f'  {msg}')
    print('-' * (len(msg) + 4))


menssagem('Eu sou Daniel Lucas')
menssagem('Graduando em Sistemas da Informação pela Estacio de Sá')
menssagem('Muito prazer!')
