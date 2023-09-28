teste = []
teste.append('Gabriel')
teste.append(28)
print(teste)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera2 = [['Mario', 52], ['Fifi', 61], ['Vitória', 30]]
for p in galera2:
    print(f'{p[0]} tem {p[1]} anos de idade.')