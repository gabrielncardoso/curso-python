time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    partidas.clear()
    jogador['nome'] = str(input('Nome do Jogador: ')).title().strip()
    tot = int(input(f'Quantas partidas {jogador["nome"].title()} jogou? '))
    for c in range(1, tot + 1):
        partidas.append(int(input(f'   Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if r in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if r in 'N':
        break
print('-=' * 30)
print('cod ', end='')
for k in jogador.keys():
    print(f'{k:<15}', end='')
print()
print('-' * 40)
for i, j in enumerate(time):
    print(f'{i:>3} ', end='')
    for v in j.values():
        print(f'{str(v):<15}', end='')
    print()
while True:
    print('-' * 40)
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    elif busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, v in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {v} gols.')
print('<<< VOLTE SEMPRE >>>')
