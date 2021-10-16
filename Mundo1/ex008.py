'''Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.'''


metros = float(input('Qual o valor ,em metros, que deseja transformar em cm e mm: '))
cm = metros*100
mm = metros*1000
print(f'O valor em metros informado é {metros}m.')
print(f'O valor em centimetros é {cm:.1f}cm.')
print(f'O valor em milimetros é {mm:.1f}mm.')