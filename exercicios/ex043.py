p = float(input('\033[;35mQual é o seu peso? (Kg) '))
a = float(input('Qual é a sua altura? (m) \033[m'))
imc = p / (a ** 2)
print('')
print('O seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif 18.5 <= imc <= 25:
    print('PARABÉNS, você está no seu PESO IDEAL!')
elif 25 < imc <= 30:
    print('Você está com SOBREPESO! Atenção!')
elif 30 < imc <= 40:
    print('Você está com OBESIDADE! Se cuide!')
else:
    print('Você está com OBESIDADE MÓRBIDA, cuidado!')
