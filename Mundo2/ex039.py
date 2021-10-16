"""
Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

print('\033[1;35m Junta Militar de Goias.\n Questionario sobre o alistamento obrigatorio.\033[m')
sexo = str(input('Você é homem ou mulher? ')).strip().lower()

from datetime import date

data = date.today().year

if sexo == 'mulher':
    print('No Brasil, o alistamento militar não é obrigatorio para mulheres.')
    print('O governo da justiça Militar agradece a sua colaboração.')
    print('-' * 50)
    exit(0)

elif sexo == 'homem':
    print('Iremos continuar com o questionario...')
ano = int(input('Digite o ano do seu nacimento: '))
print(f' Você nasceu em: {ano}, e estamos no ano de {data}. Hoje você tem {(data - ano)} anos.')
idade = data - ano

if idade < 17:
    print(f'Você ainda não precisa se alistar. Seu alistamento ocorrerá daqui {(ano - data) + 17} ano')

elif idade > 17:
    print(f'Você já deveria ter se alistado há {(data - ano) - 17} anos atrás.')
elif idade == 17:
    print(f'Está na hora de se alistar! Vá até a junta militar mais proxima de onde você mora, e aliste-se já!')
print('-' * 50)
print('O governo da justiça Militar agradece a sua colaboração.')
