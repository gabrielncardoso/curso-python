cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
while True:
    while True:
        num = int(input('Digite um número: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente.', end=' ')
    print(f'Você digitou o número {cont[num]}!')
    resp = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
            break
print('{:=^50}'.format(' FIM DO PROGRAMA '))
