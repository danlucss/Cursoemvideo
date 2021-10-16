"""
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

dados = {}
jogos = []
cont = 0
dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas o {dados["nome"]} jogou: '))
for p in range(0, partidas):
    jogos.append(int(input(f'Quantos gols ele fez na {p+1} partida? ')))


dados['gols'] = jogos[:]
dados['total'] = sum(jogos)
print('-*'*20)
print(dados)
print('-*'*20)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
print('-*'*20)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(dados['gols']):
    print(f'   => Na partida {i}, fez {v} gols.')

print(f'Foi um total de {sum(jogos)} gols.')
