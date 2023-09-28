soma = cont = 0
n = int(input('Digite um número: '))
maior = n
menor = n
soma += n
cont += 1
op = (str(input('Quer continuar? [S/N] ')))
while op in 'Ss':
    n = int(input('Digite um número: '))
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    soma += n
    cont += 1
    op = (str(input('Quer continuar? [S/N] '))).upper().strip()[0]
media = float(soma/cont)
print('Você digitou {} números e a média foi {}.'.format(cont, media))
print('O maior valor digitado foi {} e o menor foi {}.'.format(maior, menor))
