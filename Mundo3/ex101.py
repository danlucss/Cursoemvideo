"""
Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem
 voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições
"""


def voto():
    from datetime import date
    data = date.today().year
    ano = int(input('Digite o ano de seu nascimento: '))
    idade = data - ano
    if 16 <= idade < 18 or idade > 65:
        return f'Aos {idade} anos: Voto OPCIONAL!'
    elif idade >= 18:
        return f'Aos {idade} anos: Voto OBRIGATORIO!'
    elif idade <= 16:
        return f'Aos {idade} anos: Voto NEGADO!'


# programa principal
print(voto())
