d = float(input('Qual a distância da viagem? '))
p = (d*0.50) if d <= 200 else (d*0.45)
print('Você está prestes a começar uma viagem de {:.2f}Km.'.format(d).replace('.', ','))
print('O preço da sua passagem será R${:.2f}'.format(p).replace('.', ','))
