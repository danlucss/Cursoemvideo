def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print(f'\033[2;35mErro: Valido apenas números inteiros. \033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[2;35mO úsuario preferiu não informar esse número.\033[m')
            return None
        else:
            return n


def leiaReal(msg):
    while True:
        try:
            n = float(input(msg))

        except (TypeError, ValueError):
            print(f'\033[2;35mErro: Valido apenas números reais.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[2;35mO úsuario preferiu não informar esse número.\033[m')
            return None
        else:
            return n
