"""
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""

print('Calculadora - Python')
from time import sleep

print('Inicialiazndo...')
sleep(2)

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

escolha = 0
while escolha != 5:
    print('''Escolha: 
    [1] SOMA
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] FINALIZAR PROGRAMA''')
    escolha = int(input('Faça sua escolha: '))
    if escolha == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2}, é {soma}.')
    elif escolha == 2:
        mult = n1 * n2
        print(f'A multiplicação entre {n1} e {n2}, é {mult}.')
    elif escolha == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}')
    elif escolha == 4:
        print('Por favor, escolha novamente:')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número:  '))
    elif escolha == 5:
        print('Finalizando programa...')
    else:
        print('Opção invalida. Tente novamente.')
    print('=-=-' * 10)
sleep(1)
print('Programa finalizado... Obrigado.')
