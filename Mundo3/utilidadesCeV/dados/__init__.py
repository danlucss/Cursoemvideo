'''Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
 Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(),
  mas com uma validação de arquivo para aceitar apenas valores que seja monetários.'''


def leiaDinheiro(msg):
    valido = False
    while not valido:
        din = str(input(msg)).replace(',', '.')
        if din.isalpha():
            print(f'\033[1;35mERRO:\"{din}\" é um valor invalido!\033[m')
        else:
            valido = True
            return float(din)
