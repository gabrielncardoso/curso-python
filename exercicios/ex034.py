s = float(input('Qual o seu salário? R$'))
if s <= 1250:
    sn = s * 1.15
if s > 1250:
    sn = s * 1.10
print('Com o aumento, você passará a ganhar R${:.2f}'.format(sn))
