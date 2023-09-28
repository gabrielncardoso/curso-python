import math
l = float(input('Qual a largura da sua parede (em metros)? '))
h = float(input('Qual a altura da sua parede (em metros)? '))
a = l*h
v = a/2
galao = 3
print('Sua parede tem a dimensão de {:.2f}m x {:.2f}m, e sua área é {}m2'.format(l, h, a))
print('Você precisa comprar um total de {:.1f} galão(ões) de tinta.'.format(math.ceil(v/galao)))
