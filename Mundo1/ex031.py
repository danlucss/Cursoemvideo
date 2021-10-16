"""
Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
 Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
"""


print('='*50)
print('''Olá, vou ajuda-los a calcular o valor da sua passagem!
1.Para viagens abaixo de 200 KM, será cobrada a taxa será de R$0,50 por KM².
2.Para viagens acima de 200KM, será cobrada a taxa de R$0,45 por KM².''')
print('='*50)
di = float(input('Bom dia! Por favor, me informe a distancia que deseja viajar (em Km):'))

if di <= 200:
    print(f'A sua viajem é de {di} KM, por isso ela vai custar: {(di*0.5)}R$.')
else:
    print(f'A sua viagem é de {di} KM. Por isso vai custar: {di*0.45}R$.')
