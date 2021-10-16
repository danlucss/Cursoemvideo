"""
Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
 Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""

times = ['Atletico-MG', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Bragantino', 'Corinthians', 'Internacional',
         'Fluminence', 'Cuiabá', 'Athletico-PR', 'Atletico-GO', 'São Paulo', 'Ceará', 'Santos', 'Bahia', 'Juventos',
         'Gremio', 'America-MG', 'Sport', 'Chapecoense']
Chapecopos = times.index('Chapecoense') + 1
print(f"Os times do campeonato brasileiro de Futebol, em ordem de classificação são:{times}. ")
print('=-=' * 20)
print(f'Os cinco primeiros times classificados são {times[0:5]}.')
print('=-=' * 20)
print(f'Os quatro ultimos colocados são = {times[-4:]}.')
print('=-=' * 20)
print(f'Os times em ordem alfabetica são ={sorted(times)}.')
print('=-=' * 20)
print(f'O time Chapecoense está na {Chapecopos}ª posição.')
