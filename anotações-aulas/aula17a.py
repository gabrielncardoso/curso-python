valores = []
v = 1
for v in range(0, 11):
    valores.append(v)
    v += 1
valores.sort(reverse=True)
print(f'Essa lista possui os números', end=' ')
for v in valores:
    print(v, end=' ')
for c, v in enumerate(valores):
    print(f'\nNa posição {c} encontrei o valor {v}.')
print('Cheguei ao final da lista.')
