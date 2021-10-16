"""Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
 o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
  indicando se será mostrado ou não na tela o processo de cálculo do fatorial."""


# Função
def fatorial(num=1, show=True):
    """
    -> Indica o fatorial de um número escolhido.
    :param num: Insira o número inteiro positivo para somar seu fatorial.
    :param show: Caso esteja ativado, (com True), indica a formação do fatorial. Caso desativado, mostra apenas o
    resultado.
    """

    f = 1
    for c in range(num, 0, -1):
        f *= c

    for c in range(num, 0, -1):
        if show:
            print(f'{c} ', end='')
            print('x ' if c > 1 else '=', end='')

        else:
            print(f'O fatorial de {num} é =', end='')
            break
    print(f' {f}.')


n = int(input('Insira um número: '))
help(fatorial)
