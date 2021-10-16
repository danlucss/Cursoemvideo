from menu import interface
from time import sleep

while True:
    resposta = interface.menu(['Ver Pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        print(interface.titulo('OPÇÃO 1'))
    elif resposta == 2:
        print(interface.titulo('OPÇÃO 2'))
    elif resposta == 3:
        print(interface.titulo('SAINDO DO PROGRAMA... ATÉ LOGO!'))
        break
    else:
        print('ERROR! Digite uma opção valida')
    sleep(2)