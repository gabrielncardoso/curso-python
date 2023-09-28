lista = []
for num in range(0, 5):
    lista.append(int(input(f'Digite um valor para a Posição {num}: ')))
print('=-'*30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições', end=' ')
for pos, num in enumerate(lista):
    if num == max(lista):
        print(pos, end='...')
print(f'\nO menor valor digitado foi {min(lista)} nas posições', end=' ')
for pos, num in enumerate(lista):
    if num == min(lista):
        print(pos, end='...')
