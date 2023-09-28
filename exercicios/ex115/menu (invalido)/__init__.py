def titulo(msg):
    print('-' * 40)
    print(msg.center(40))
    print('-' * 40)


def menu():
    from time import sleep
    while True:
        titulo('MENU PRINCIPAL')
        print('1 - Ver pessoas cadastradas')
        print('2 - Cadastrar nova pessoa')
        print('3 - Sair do sistema')
        print('-' * 40)
        while True:
            try:
                op = int(input('Sua opção: '))
            except:
                print('ERRO: por favor, digite um número inteiro válido.')
            else:
                if 1 <= op <= 2:
                    titulo(f'Opção {op}')
                    sleep(1)
                    break
                elif op == 3:
                    titulo('Saindo do programa...')
                    sleep(1)
                    break
                else:
                    print('ERRO! Digite uma opção válida.')
                    sleep(1)
                    break
        if op == 3:
            break
