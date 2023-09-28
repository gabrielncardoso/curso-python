print('Bem vindo(a), ao CONVERSOR DE MEDIDAS\n')
n = float(input('Digite uma medida em metros: '))
km = n * 0.001
hm = n * 0.01
dam = n * 0.1
dm = n * 10
cm = n * 100
mm = n * 1000
print('A medida de {:.2f}m corresponde a:'.format(n))
print('{}km' .format(km))
print('{}hm' .format(hm))
print('{:.2f}dam' .format(dam))
print('{}dm' .format(dm))
print('{}cm' .format(cm))
print('{}mm' .format(mm))
print('\nObrigado por utilizar o CONVERSOR DE MEDIDAS!')
