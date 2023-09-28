from random import randint
from time import sleep
from operator import itemgetter
jogadas = {}
ranking = []
print('Valores sorteados: ')
for c in range(1, 5):
    jogadas[f'jogador{c}'] = randint(1, 6)
for k, v in jogadas.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'    {i+1}o. lugar: {v[0]} com {v[1]}.')
    sleep(0.5)
