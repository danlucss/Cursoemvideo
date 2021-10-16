def titulo(msg):
    print('—' * 50)
    print(msg.center(50))
    print('—' * 50)


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except FileExistsError:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except FileNotFoundError:
        print('Houve um ERRO na leitura do arquivo.')
    else:
        titulo('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'Nome: {dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except FileNotFoundError:
        print('Houve um ERRO ao abrir o arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except FileExistsError:
            print('Houve um erro na hora de escrever os dados.')
        else:
            print(f'Novo registro de {nome} adcionado.')
            a.close()
