v = float(input('Valor da casa: R$'))
s = float(input('Salário do comprador: R$'))
t = int(input('Quantos anos de financiamento? '))
pm = v / (t*12)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}.'.format(v, t, pm))
if pm <= s*0.30:
    print('\033[1;32mParabéns! O seu empréstimo foi APROVADO!\033[m')
else:
    print('\033[1:31mDesculpa, seu empréstimo foi NEGADO!\033[m')
