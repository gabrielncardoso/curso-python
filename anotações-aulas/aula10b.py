n1 = int(input('Digite sua primeira nota: '))
n2 = int(input('Digite sua segunda nota: '))
m = (n1 + n2)/2
print('Sua média foi {:.1f}'.format(m))
if m >= 9.0:
    print('Sua média foi EXCELENTE!')
if 6.0 >= m < 9.0:
    print('Sua média foi boa. Parabéns!')
if m < 6.0:
    print('Sua média foi ruim. Estude mais!')
