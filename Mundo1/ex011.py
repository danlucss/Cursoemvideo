'''
Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
'''

lar = float(input('Qual a largura da parede: '))
alt = float(input('Qual a altura da parede: '))
area = lar * alt
tinta = area/2
print(f'Sua parede tem {lar}m de largura e {alt}m de altura. A área total é de {area}m.')
print(f'Serão necessarios {tinta} latas de tinta para pintar a parede.')
