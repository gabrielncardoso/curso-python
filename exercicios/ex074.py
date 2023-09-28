from random import randint
sorteio = (randint(0, 10), randint(0, 10), randint(0, 10),
           randint(0, 10), randint(0, 10))
organizado = sorted(sorteio)
print('Os valores sorteados foram: ', end='')
for c in sorteio:
    print(c, end=' ')
print(f'\nO maior valor sorteado foi {organizado[-1]}')
print(f'O menor valor sorteado foi {organizado[0]}')
