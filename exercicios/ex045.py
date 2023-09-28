import random
from time import sleep
print('''Suas opçÕes:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jog = str(input('Qual é a sua jogada? ').replace('0', 'Pedra').replace('1', 'Papel').replace('2', 'Tesoura'))
if jog != 'Pedra' and jog != 'Papel' and jog != 'Tesoura':
    print('OPÇÃO INVÁLIDA')
else:
    lista = ['Pedra', 'Papel', 'Tesoura']
    comp = random.choice(lista)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    print('-='*15)
    print('Computador jogou {}'.format(comp))
    print('Jogador jogou {}'.format(jog))
    print('-='*15)
    if jog == 'Pedra' and comp == 'Tesoura' or jog == 'Papel' and comp == 'Pedra' or jog == 'Tesoura' and comp == 'Papel':
        r = 'JOGADOR VENCE'
    elif comp == 'Pedra' and jog == 'Tesoura' or comp == 'Tesoura' and jog == 'Papel' or comp == 'Papel' and jog == 'Pedra':
        r = 'COMPUTADOR VENCE'
    else:
        r = 'EMPATE'
    print(r)
