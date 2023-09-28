print('-=-' * 10)
print('\033[1;34;43mANALISADOR DE TRIÂNGULOS\033[m')
print('-=-' * 10)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if (b-c) < a < (b+c) and (a-c) < b < (a+c) and (a-b) < c < (a+b):
    print('Os segmentos acima podem formar um triângulo :)')
else:
    print('Os segmentos acima NÃO podem formar um triângulo')
