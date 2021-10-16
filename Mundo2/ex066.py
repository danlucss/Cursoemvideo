"""
Exercício Python 66: Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).


"""

cont = soma = maior = menor = 0

while True:
    n = int(input('Digite um valor [Digite 999 para parar]:  '))
    if n == 999:
        break
    cont += 1
    soma += n

    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print(f'Foram digitados {cont} valores. A soma entre eles é de {soma}.')
