print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
n50 = n20 = n10 = n1 = 0
valor = int(input('Qual valor você quer sacar? R$'))
while True:
    if valor - 50 >= 0:
        n50 += 1
        valor -= 50
    elif valor - 50 < 0:
        if valor - 20 >= 0:
            n20 += 1
            valor -= 20
        elif valor - 20 < 0:
            if valor - 10 >= 0:
                n10 += 1
                valor -= 10
            elif valor - 10 < 0:
                    if valor - 1 >= 0:
                        n1 += 1
                        valor -= 1
                    elif valor - 1 < 0:
                        break
if n50 > 0:
    print(f'Total de {n50} cédulas de R$50')
if n20 > 0:
    print(f'Total de {n20} cédulas de R$20')
if n10 > 0:
    print(f'Total de {n10} cédulas de R$10')
if n1 > 0:
    print(f'Total de {n1} cédulas de R$1')
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
