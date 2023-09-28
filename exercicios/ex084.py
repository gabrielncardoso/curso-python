galera = []
maispesado = []
menospesado = []
maior = menor = 0
while True:
    pessoa = []
    pessoa.append(str(input('Nome: ').title()))
    peso = float(input('Peso: '))
    pessoa.append(peso)
    if len(galera) == 0:
        maispesado.append(pessoa)
        menospesado.append(pessoa)
    else:
        if pessoa[1] == maispesado[0][1]:
            maispesado.append(pessoa)
        elif pessoa[1] > maispesado[0][1]:
            maispesado.clear()
            maispesado.append(pessoa)
        if pessoa[1] == menospesado[0][1]:
            menospesado.append(pessoa)
        elif pessoa[1] < menospesado[0][1]:
            menospesado.clear()
            menospesado.append(pessoa)
    galera.append(pessoa)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'N':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(galera)} pessoas.')
print(f'O maior peso foi de {maispesado[0][1]}kg. Peso de', end=' ')
for p in maispesado:
    print(p[0], end=' ')
print()
print(f'O menor peso foi de {menospesado[0][1]}kg. Peso de', end=' ')
for p in menospesado:
    print(p[0], end=' ')
