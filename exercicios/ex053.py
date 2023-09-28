frase = input('Digite uma frase: ').strip().upper().replace(' ', '')
fraseinv = frase[::-1].strip().upper().replace(' ', '')
print('O inverso de {} é {}'.format(frase, fraseinv))
if frase == fraseinv:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
