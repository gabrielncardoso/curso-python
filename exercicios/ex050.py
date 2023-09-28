soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {} valor: '.format(c)))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
if cont == 1:
    print('Você informou {} número par, que foi o número {}!'.format(cont, soma))
else:
    print('Você informou {} números pares, e a soma deles é igual a {}!'.format(cont, soma))
