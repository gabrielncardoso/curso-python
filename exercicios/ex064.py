n = cont = soma = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        soma += n
        cont += 1
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))
