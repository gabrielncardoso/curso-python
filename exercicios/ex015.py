d = int(input('Quantos dias você ficou com o carro? '))
k = float(input('Quantos km você rodou? '))
vd = 60 * d
vk = 0.15 * k
vt = vd + vk
print('O valor total a pagar é de R${:.2f}'.format(vt))
