# FAZER SEM O MATH FACTORIAL, USANDO WHILE
n = int(input('Digite um número para calcular seu fatorial: '))
print('Calculando fatorial de {}! '.format(n), end='')
c = n
f = 1  # FATOR NEUTRO DE MULTIPLICAÇÃO É 1
while c > 0:
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)
