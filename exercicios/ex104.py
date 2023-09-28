def leiaInt(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            return num
            break
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido\033[m')


# PROGRAMA PRINCIPAL
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
