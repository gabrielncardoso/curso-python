print('\033[7;34;45m{:=^40}\033[m'.format(' MERCADINHO GABRIEL '))
p = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO)
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
o =int(input('Digite a opção desejada: '))
if o == 1:
    t = p * 0.90
elif o == 2:
    t = p * 0.95
elif o == 3:
    t = p
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS!'.format(p / 2))
elif o == 4:
    t = p * 1.2
    par = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS!'.format(par, (t / par)))
print('Com essa forma de pagamento, a sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(p, t))
