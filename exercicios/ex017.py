from math import hypot
'''ca = float(input('Digite a medida do cateto adjacente: '))
co = float(input('Digite a medida do cateto oposto: '))
hip = math.sqrt((ca**2) + (co**2))
print('A medida da hipotenusa é {:.2f}'.format(hip))'''

ca = float(input('Digite a medida do cateto adjacente: '))
co = float(input('Digite a medida do cateto oposto: '))
hi = hypot(ca, co)
print('A medida da hipotenusa é {:.2f}'.format(hi))
