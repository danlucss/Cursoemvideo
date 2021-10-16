"""Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar
 de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
 Ex: n = leiaInt(‘Digite um n: ‘)"""


def leiaInt(msg):
    '''
    Função para imprimir na tela um número inteiro;
    :param msg: Retorna a mensagem desejada.
    :return: Caso o número informado seja inteiro, ela retorna o número, senão, ela entra em loop, até um número inteiro
    valido ser selecionado.
    '''
    while True:
        a = str(input(msg))
        if a.isnumeric():
            return int(a)
        else:
            print(f'\033[35mErro. Válido apenas números inteiros.\033[m')


n = leiaInt('Digite um número inteiro: ')
print(f'O número informado foi {n}.')
