"""
Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""

c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while True:
    n = int(input('Digite um número para ver sua tabuada: [Para sair, digite um número negativo] '))
    if n < 0:
        break
    print('==' * 20)
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('==' * 20)
print('Programa finalizado. Obrigado.')
