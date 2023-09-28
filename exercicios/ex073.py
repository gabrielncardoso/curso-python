tabela = ('Coritiba', 'Ceará', 'Flamengo', 'Atlético Goianiense',
          'Santos', 'Fluminense', 'América-MG', 'Athletico-PR',
          'Atlético Mineiro', 'Avaí', 'Botafogo', 'Corinthians',
          'Cuiabá', 'Fortaleza', 'Internacional', 'Juventude',
          'Bragantino', 'São Paulo', 'Palmeiras', 'Goiás')
print('-=' * 20)
print(f'Lista de times do Brasileirão: {tabela}')
print('-=' * 20)
print(f'Os 5 primeiros colocados são: {tabela[:5]}')
print('-=' * 20)
print(f'Os 4 últimos colocados são: {tabela[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-=' * 20)
print(f'O Fortaleza está na {tabela.index("Fortaleza")+1}a posição')
