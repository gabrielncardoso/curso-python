a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# VERIFICANDO QUEM É MENOR
menor = a
if b < c and b < a:
    menor = b
if c < a and c < b:
    menor = c
# VERIFICANDO QUEM É MAIOR
maior = a
if b > a and b > c:
    maior = b
if c > b and c > a:
    maior = c
print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))
