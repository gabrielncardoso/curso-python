# ANALISANDO TRIANGULO V2.0
print('\033[1;35m-=-' * 10)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-' * 10)
print('\033[m')
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a == b == c:
    t = 'EQUILÁTERO'
elif a == b != c or a == c != b or b == c != a:
    t = 'ISÓSCELES'
elif a != b != c != a:
    t = 'ESCALENO'
print('\033[1;35mPROCESSANDO...\033[m')
if (b-c) < a < (b+c) and (a-c) < b < (a+c) and (a-b) < c < (a+b):
    print('Os segmentos acima PODEM FORMAR um triângulo {}!'.format(t))
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')
