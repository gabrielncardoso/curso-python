galera = []
totmai = totmen = 0
for c in range(0, 3):
    dado = []
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado)
for p in galera:
    if p[1] > 18:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Ao todo temos {totmai} maiores de idade, e {totmen} menores de idade!')
