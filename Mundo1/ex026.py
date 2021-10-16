'''Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
 em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''

f= str(input('Escreva uma frase:')).strip().lower()
f1= f.lower().count('a')
f2= f.find('a')
f3= f.rfind('a')
print (f'A sua frase é {f} e nela contém {f1} letras A ')
print(f'O primeiro a aparece na posição {f2}')
print(f'O ultimo a aparece na posição {f3}')