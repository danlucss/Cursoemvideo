"""
Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposenta
"""


from datetime import datetime as dt

dados = {'nome': str(input('Nome: '))}
nasc = int(input('Ano de nascimento: '))
dados['idade'] = dt.now().year - nasc
dados['CTPS'] = int(input('Informe o nº da CTPS [0 para não tem]: '))
if dados['CTPS'] != 0:
    dados['nome da empresa'] = str(input('Nome da empresa: '))
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salario: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - dt.now().year)
print('-*'*20)
for k, v in dados.items():
    print(f' - {k} tem o valor: {v}.')
