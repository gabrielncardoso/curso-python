import random
from time import sleep # faz o programa dormir por alguns segundos
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
n = random.randint(0, 5) # FAZ O COMPUTADOR ESCOLHER UM NUMERO
a = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if a == n:
    print('Parabéns! Você conseguiu me vencer!')
if n != a < 5:
    print('Que pena! O número era {}. Eu ganhei :)'.format(n))
if a > 5:
    print('Não vale! Eu falei entre 0 e 5!!!')
# Quero adicionar uma mensagem que apareça caso o jogador digite um numero real (float)
