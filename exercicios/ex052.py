cont = 0
print('ANALISADOR DE NÚMEROS PRIMOS')
n = int(input('Digite um número para ser analisado: '))
for c in range(1, n+1):
    if n % c == 0:
        print('\033[32m', end=' ')
        cont = cont + 1
    if n % c != 0:
        print('\033[1;31m', end=' ')
    print(c, end=' ')
print('\033[m')
print('O número {} foi divisível {} vezes'.format(n, cont))
if cont == 2:
    print('E por isso ele é um número PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')
