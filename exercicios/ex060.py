# CALCULO DO FATORIAL
from math import factorial
n = int(input('''Digite um número para
calcular seu fatorial: '''))
fat = factorial(n)
print('Calculando {}!'.format(n), end=' = ')
for n in range(n, 0, -1):
    if n != 1:
        print(n, end=' x ')
    elif n == 1:
        print(n, end=' = ')
print(fat)
