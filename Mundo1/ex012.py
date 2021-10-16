'''Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''

p= float(input('Qual o valor do produto?'))
d= p*0.05
print (f'O preço do produto é \033[35m {p} \033[m porém com o desconto de 5% ele sai a {p-d:.2f}.')