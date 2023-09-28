hmaisv = ''.capitalize().join(', ')
idadehv = 0
mmenor = 0
itotal = 0
for c in range(1, 5):
    print('-----{}a PESSOA-----'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ').upper())
    itotal += idade
    if sexo in 'Mm': # se o usuário digitar M ou m
        if c == 1:
            hmaisv = nome
            idadehv = idade
        else:
            if idade > idadehv:
                hmaisv = nome
                idadehv = idade
    if sexo == 'F' and idade < 20:
        mmenor += 1
imedia = float(itotal/c)
print('A idade média do grupo é de {} anos'.format(imedia))
print('O homem mais velho tem {} anos e seu nome é {}!'.format(idadehv, hmaisv))
if mmenor == 1:
    print('Ao todo tem {} mulher com menos de 20 anos!'.format(mmenor))
else:
    print('Ao todo tem {} mulheres com menos de 20 anos!'.format(mmenor))
