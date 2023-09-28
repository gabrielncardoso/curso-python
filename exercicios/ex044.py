print('\033[7;34;45m{:=^40}\033[m'.format(' MERCADINHO GABRIEL '))
p = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO)
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
o =int(input('Digite a opção desejada: '))
if o == 1:
    print('Com essa forma de pagamento, a sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(p, (p * 0.90)))
elif o == 2:
    print('Com essa forma de pagamento, a sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(p, (p * 0.95)))
elif o == 3:
    print('Sua compra será parcelada em 2x de R${:.2f}.'.format(p / 2))
    print('Para parcelar em 2 vezes no cartão, a sua compra de R${:.2f} continuará custando R${:.2f} no final.'.format(p, p))
elif o == 4:
    par = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de R${} COM JUROS!'.format(par, (p * 1.2 / par)))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(p, (p * 1.2)))
else:
    print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE.')
