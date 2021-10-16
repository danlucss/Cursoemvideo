"""
Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista
única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""

principal = [[], []]

for p in range(0, 7):
    pergunta = int(input(f'Digite o {p} valor: '))
    if pergunta % 2 == 0:
        principal[0].append(pergunta)
    else:
        principal[1].append(pergunta)
principal[0].sort()
principal[1].sort()
print('*'*40)
print(f'Os valores pares e impares, respectivamente, são:\033[32m {principal}\033[m.')
