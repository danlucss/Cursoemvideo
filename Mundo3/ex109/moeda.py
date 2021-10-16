'''
Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro()
 e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.'''


def aumentar(preco=0, taxa=0, format=False):
    '''
    ->Função para aumentar um valor de acordo com a taxa.
    :param preco: O valor a ser aumentado.
    :param taxa: A porcentagem do valor a ser aumentado.
    :param format: *Parametro opcional, caso ativo, devolve o valor formatado.
    :return: Retorna o valor com aumento, e formatado, caso solicitado.
    '''
    res = preco + (preco * taxa / 100)
    return res if format is False else moeda(res)


def diminuir(preco=0, taxa=0, format=False):
    '''
    ->Função para aumentar um valor de acordo com a taxa.
    :param preco: O valor a ser aumentado.
    :param taxa: A porcentagem do valor a ser aumentado.
    :param format: *Parametro opcional, caso ativo, devolve o valor formatado.
    :return: Retorna o valor diminuido, e formatado, caso solicitado.
    '''
    res = preco - (preco * taxa / 100)
    return res if format is False else moeda(res)


def dobro(preco=0, format=False):
    '''
    ->Função para dobrar o valor requisitado.
    :param preco: O valor a ser dobrado.
    :param format:  *Parametro opcional, caso ativo, devolve o valor formatado.
    :return: Retorna o valor dobrado, e formatado, caso solicitado.
    '''
    res = preco * 2
    return res if format is False else moeda(res)


def metade(preco=0, format=False):
    '''
    ->Função que mostra a metade do valor solicitado.
    :param preco: Valor a ser dividido.
    :param format:  *Parametro opcional, caso ativo, devolve o valor formatado.
    :return: Retorna o valor pela metade, e formatado, caso solicitado.
    '''
    res = preco / 2
    return res if format is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    '''
    ->Função para formatar valores monetarios.
    :param preco: Valor a ser formatado.
    :param moeda: Moeda a ser utilizada para a formatação.
    :return: Retorna o valor formatado.
    '''
    return f'{moeda}{preco:.2f}'.replace('.', ',')
