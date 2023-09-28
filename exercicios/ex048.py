soma = 0  # acumulador
cont = 0  # contador
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1 # ou pode ser cont += 1
        soma = soma + c # ou soma += 1
        print(c, end=' ')
print('\nA soma dos {} valores solicitados é {}!'.format(cont, soma))
