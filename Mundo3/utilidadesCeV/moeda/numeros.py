
def aumentar(preço=0, taxa1=0, format=False):
    '''
    ->Função para aumentar um valor de acordo com a taxa.
    :param preço: O valor a ser aumentado.
    :param taxa1: A porcentagem do valor a ser aumentado.
    :param format: *Parametro opcional, caso ativo, devolve o valor formatado.
    :return: Retorna o valor com aumento, e formatado, caso solicitado.
    '''
    res = preço + (preço * taxa1/100)
    return res if format is False else moeda(res)


def diminuir(preço=0, taxa2=0, format=False):
    '''
    ->Função para aumentar um valor de acordo com a taxa.
    :param preço: O valor a ser aumentado.
    :param taxa2: A porcentagem do valor a ser aumentado.
    :param format: *Parametro opcional, caso ativo, devolve o valor formatado.
    :return: Retorna o valor diminuido, e formatado, caso solicitado.
    '''
    res = preço - (preço * taxa2/100)
    return res if format is False else moeda(res)


def dobro(preço=0, format=False):
    '''
    ->Função para dobrar o valor requisitado.
    :param preço: O valor a ser dobrado.
    :param format:  *Parametro opcional, caso ativo, devolve o valor formatado.
    :return: Retorna o valor dobrado, e formatado, caso solicitado.
    '''
    res = preço * 2
    return res if format is False else moeda(res)


def metade(preço=0, format=False):
    '''
    ->Função que mostra a metade do valor solicitado.
    :param preço: Valor a ser dividido.
    :param format:  *Parametro opcional, caso ativo, devolve o valor formatado.
    :return: Retorna o valor pela metade, e formatado, caso solicitado.
    '''
    res = preço / 2
    return res if format is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    '''
    ->Função para formatar valores monetarios.
    :param preço: Valor a ser formatado.
    :param moeda: Moeda a ser utilizada para a formatação.
    :return: Retorna o valor formatado.
    '''
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def titulo(msg):
    print('-'*30)
    print(msg.center(30))
    print('-'*30)


def resumo(preço=0, taxa1=0, taxa2=0):
    titulo('Resumo do valor')
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxa1}% de aumento: \t{aumentar(preço, taxa1, True)}')
    print(f'{taxa2}% de redução:  \t{diminuir(preço, taxa2, True)}')
    print('-'*30)
