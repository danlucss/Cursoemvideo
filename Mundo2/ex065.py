"""
Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""

S = 'S'
cont = soma = med = 0
maior = 0
menor = 0

while S in 'Ss':
    n = int(input('Digite um número inteiro: '))
    cont += 1
    soma += n
    maior = n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    S = str(input('Quer continuar? [S/N]')).strip()
med = soma / cont
print(f'Foram digitatos {cont} números, e a média entre eles é de {med:.2f}. O menor número é {menor}, e o maior '
      f'número é {maior}.')
