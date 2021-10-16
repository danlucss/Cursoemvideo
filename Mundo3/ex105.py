"""Exercício Python 105: Faça um programa que tenha uma função notas() que
pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)
"""


def notas(*n, sit=False):
    '''
    -> Função para analisar notas e situações de varios alunos.
    :param n: Uma ou mais notas de alunos(aceita varias).
    :param sit: valor opicional, indica se deve ou não retornar a situação dos alunos
    :return: dicionario, com varias informações sobre a situação dos alunos.
    '''
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Media'] = sum(n) / len(n)

    if sit:
        if r['Media'] >= 7:
            r['situação'] = 'Boa'
        elif r['Media'] >= 5:
            r['situação'] = 'Razoavel'
        else:
            r['situação'] = 'Ruim'

    return r


resp = notas(10, 6, 8.1, 9, 10, sit=True)
print(resp)
