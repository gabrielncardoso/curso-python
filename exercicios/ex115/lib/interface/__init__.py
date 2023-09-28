def verde():
    return '\033[32m'


def amarelo():
    return '\033[33m'


def azul():
    return '\033[34m'


def vermelho():
    return '\033[1;31m'


def semcor():
    return '\033[m'


def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
            continue  # FAZ CONTINUAR O LAÇO (TESTEI SEM E FUNCIONOU)
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return num


def linha(tam=42):
    print('-' * tam)


def cabeçalho(txt):
    linha()
    print(txt.center(42))
    linha()


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{amarelo()}{c}{semcor()} - {azul()}{item}{semcor()}')
        c +=1
    linha()
    opc = leiaInt(f'{verde()}Sua opção: {semcor()}')
    return opc
