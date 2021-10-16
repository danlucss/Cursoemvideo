"""
Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.


"""


from time import sleep
print('Contagem regressiva para os fogos de fim de ano!!!')
for c in range(10, 0, -1):
    sleep(1)
    print(c)
print('\033[2;31m*-\033[m'*15)
print('Boas festas de ano novo!')
