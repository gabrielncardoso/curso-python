# ANALISANDO TRIANGULO V2.0
from time import sleep
print('\033[1;35m-=-' * 10)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-' * 10)
print('\033[m')
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
print('\033[1;35mPROCESSANDO...\033[m')
sleep(1)
if (b-c) < a < (b+c) and (a-c) < b < (a+c) and (a-b) < c < (a+b):
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if a == b == c:
        print('EQUILÁTERO!')
    elif a != b and a != c and b != c:
        print('ESCALENO!')
    elif a == b != c or a == c != b or b == c != a:
        print('ISÓCELES!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')
