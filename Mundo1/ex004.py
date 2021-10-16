'''Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
 e todas as informações possíveis sobre ele.'''


p = input('Digite alguma coisa: ')
print('A palavra é: {}{}{}'.format('\033[35m', p ,'\033[m'))
print ('O tipo primitivo dessa palavra é:',type(p))
print('É uma maiuscula?',p.isupper())
print('Está em letra minuscula?',p.islower())
print('É um titulo?',p.istitle())
print('Só tem espaço?', p.isspace())