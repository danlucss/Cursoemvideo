"""
Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

doces = ('brigadeiro', 'beijinho', 'sorvete', 'pudim', 'flan', 'chocolate', 'caramelo')

for palavras in doces:
    print(f'Palavras =  {palavras.upper()}\n Vogais:', end='')
    for letras in palavras:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')
    print('\n')
