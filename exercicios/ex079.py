listanum = []
while True:
    listanum.append(int(input('Digite um valor: ')))
    if listanum[-1] in listanum[:-1]:
        print('Valor duplicado! Não vou adicionar...')
        listanum.pop()
    else:
        print('Valor adicionado com sucesso...')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resp in 'N':
        break
print('=-' * 30)
listanum.sort()
print(f'Você digitou os números {listanum}')
