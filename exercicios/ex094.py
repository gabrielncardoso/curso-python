dados = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).title()
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    dados.append(pessoa.copy())
    while True:
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if r in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if r == 'N':
        break
print('-=' * 30)
media = soma / len(dados)
print(f'A) Ao todo temos {len(dados)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in dados:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print()
print('D) Lista das pessoas que estão acima da média:')
for p in dados:
    if p['idade'] > media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
        print()
print('<< ENCERRADO >>')
