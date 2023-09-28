dados = {}
listagols = []
dados['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {dados["nome"].title()} jogou? '))
for c in range(1, tot + 1):
    listagols.append(int(input(f'   Quantos gols na partida {c}? ')))
dados['gols'] = listagols[:]
dados['total'] = sum(listagols)
print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {dados["nome"]} jogou {len(dados["gols"])} partidas.')
for i, v in enumerate(dados['gols']):
    print(f'   => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols.')
