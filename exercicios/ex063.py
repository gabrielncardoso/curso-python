print('-'*30)
print('SEQUÊNCIA DE FIBONACCI')
print('-'*30)
termo = int(input('Quantos termos você quer mostrar? '))
n1 = 0
n2 = 1
cont = 3
print('~'*30)
print('{} -> {} -> '.format(n1, n2), end='')
while cont <= termo:
    n3 = n2 + n1
    print(n3, end=' -> ')
    n1 = n2
    n2 = n3
    cont += 1
print('FIM')
print('~'*30)
