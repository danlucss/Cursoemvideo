def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print(f'\033[2;35mErro: Valido apenas números inteiros. \033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[2;35mO úsuario preferiu não informar esse número.\033[m')
            return 0
        else:
            return n


def linha(tam=50):
    return '—' * tam


def titulo(msg):
    print('—'*50)
    print(msg.center(50))
    print('—'*50)


def menu(lista):
    titulo('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[31m{c}\033[m — \033[32m{item}\033[m')
        c += 1
    print(linha())
    resp = leiaInt(f'\033[33mSua Opção:\033[m ')
    return resp
