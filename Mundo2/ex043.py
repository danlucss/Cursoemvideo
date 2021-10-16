"""
Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida
"""


print('Calculadora de IMC')
from time import sleep
print('Inicializando...')
sleep(1)
p = float(input('Por favor, informe seu peso: '))
a = float(input('Por favor, informe sua altura: '))
IMC = p / (a**2)
print('Calculando...')
sleep(1)
print(f'O seu peso é {p:.2f}Kg e sua altura é {a:.2f}cm.\n O seu IMC é de {IMC:.2f}.')

if IMC < 18.5:
    print('Você está abaixo do peso. PERIGO!')
elif IMC < 25:
    print('Você está em seu peso ideal! Muito bem!')
elif IMC < 30:
    print('Você está com sobrepeso. Precisa se cuidar mais!')
elif IMC < 40:
    print('Você está obeso. Tome muito cuidado.')
elif IMC > 40:
    print('PERIGO! OBESIDADE MORBIDA! POR FAVOR, PROCURE UM MEDICO IMEDIATAMENTE!')
