from arquivo import *
from interface import *
from time import sleep

arquivo = 'Pessoas Cadastradas.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)


while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arquivo)

    elif resposta == 2:
        titulo('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arquivo, nome, idade)

    elif resposta == 3:
        titulo('SAINDO DO PROGRAMA... ATÉ LOGO!')
        break

    else:
        print('ERROR! Digite uma opção valida')
    sleep(2)
