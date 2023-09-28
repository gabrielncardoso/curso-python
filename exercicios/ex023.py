n = int(input('Informe um número: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Analisando o número {}...'.format(n))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

'''print('Unidade: {}'.format(numero[len(numero)-1:len(numero)]))
print('Dezena: {}'.format(numero[len(numero)-2:len(numero)-1]))
print('Centena: {}'.format(numero[len(numero)-3:len(numero)-2]))
print('Milhar: {}'.format(numero[len(numero)-4:len(numero)-3]))'''
