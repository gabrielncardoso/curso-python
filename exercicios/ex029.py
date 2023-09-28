v = float(input('Velocidade registrada: '))
m = (v - 80)*7
if v > 80:
    print('OPA! VOCÊ FOI MULTADO! O limite de velocidade é de 80km/h')
    print('Você deve pagar uma multa de R${:.2f}.'.format(m))
print('Tenha um bom dia! Dirija com segurança')
