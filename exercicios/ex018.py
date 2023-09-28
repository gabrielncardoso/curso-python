from math import sin, cos, tan, degrees, radians
a = float(input('Digite um ângulo: '))
an = radians(a)
print('O ângulo de {}º tem o Seno de {:.2f}'.format(an, sin(an)))
print('O ângulo de {}º tem o Cosseno de {:.2f}'.format(an, cos(an)))
print('O ângulo de {}º tem a Tangente de {:.2f}'.format(an, tan(an)))
