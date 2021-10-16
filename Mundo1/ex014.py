'''Exercício Python 14: Escreva um programa que converta uma
 temperatura digitando em graus Celsius e converta para graus Fahrenheit.'''

c= float(input('Qual a temperatura em C°?'))
f= ((9*c)/5) +32
print (f'Se a temperatura em C° é {c}C°, ela será{f:.2f}F° em F°')