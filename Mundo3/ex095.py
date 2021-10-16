"""
Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de
visualização de detalhes do aproveitamento de cada jogador.
"""

times = list()
dados = {}
jogos = []

while True:
    dados.clear()
    dados['nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantas partidas o {dados["nome"]} jogou: '))
    jogos.clear()
    for p in range(0, total):
        jogos.append(int(input(f'Quantos gols ele fez na {p + 1} partida? ')))
    dados['gols'] = jogos[:]
    dados['total'] = sum(jogos)
    times.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in "SN":
            break
        print('ERROR! Por favor, digite apenas S ou N.')
    if resp == 'N':
        break

print('-*' * 20)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(times):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-*' * 20)
while True:
    busca = int(input('Mostrar arquivo de qual jogador: [999 para parar]'))
    if busca == 999:
        break
    if busca >= len(times):
        print('Erro! Não existe dado para esse jogador.')
    else:
        print(f' -- Levantamento do jogador {times[busca]["nome"]}:')
        for i, g in enumerate(times[busca]['gols']):
            print(f'   No jogo {i + 1} fez {g} gols.')
        print('' * 40)
print('<<<VOLTE SEMPRE>>>')

'''print('-*'*20)
print(f'O jogador {arquivo["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(arquivo['gols']):
    print(f'   => Na partida {i}, fez {v} gols.')

print(f'Foi um total de {sum(jogos)} gols.')'''
