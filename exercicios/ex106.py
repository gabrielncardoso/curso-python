from time import sleep
c = ('\033[m',         # 0 - SEM COR
     '\033[1;30;41m',  # 1 - VERMELHO
     '\033[1;30;42m',  # 2 - VERDE
     '\033[1;30;43m',  # 3 - AMARELO
     '\033[1;30;44m',  # 4 - AZUL
     '\033[1;30;45m',  # 5 - ROXO
     '\033[1;30;47m'   # 6 - BRANCO
     )


def mensagem(msg, cor=0):
    print(c[cor], end='')
    print('~' * (len(msg) + 4))
    print(f'  {msg}')
    print('~' * (len(msg) + 4))
    print(c[0], end='')


def pyhelp():
    mensagem('SISTEMA DE AJUDA PyHELP', 2)
    while True:
        r = str(input('Função ou Biblioteca > '))
        if r.upper() == 'FIM':
            break
        mensagem(f"Acessando o manual de comando '{r}'", 4)
        sleep(2)
        print(c[6])
        help(r)
        print(c[0], end='')
        sleep(1)
    mensagem('ATÉ LOGO!', 1)
    sleep(1)


# PROGRAMA PRINCIPAL
pyhelp()
