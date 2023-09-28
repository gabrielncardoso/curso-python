# ESTRUTURA DE REPETIÇÃO WHILE
'''for c in range(1, 10):
    print(c)
print('FIM')'''
''''from time import sleep
c = 1
while c < 10:
    print(c)
    c += 1
    sleep(1)
print('FIM')'''

'''n = 1
while n != 0: # NESSE CASO O 0 É O FLAG - CONDIÇÃO DE PARADA
    n = int(input('Digite um valor: '))
print('FIM')'''

''''r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
print('Fim')'''

n = 1
par = imp = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            imp += 1
print('Você digitou {} números pares.'.format(par))
print('E digitou {} números ímpares'.format(imp))
print('Fim')
