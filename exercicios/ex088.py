from random import randint
from time import sleep
print('-' * 30)
print(f"{'JOGA NA MEGA SENA':^30}")
print('-' * 30)
n = int(input('Quantos jogos você quer que eu sorteie? '))
jogos = []
for j in range(0, n):
    jogo = []
    while len(jogo) < 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    jogo.sort()
    jogos.append(jogo)
print('-=' * 3, f'SORTEANDO {n} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE >', '-=' * 5)
