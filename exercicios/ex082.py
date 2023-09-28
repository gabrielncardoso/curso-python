lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um número: ')))
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if r in 'N':
        break
for pos, n in enumerate(lista):
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print('-=' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
