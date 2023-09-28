from datetime import date
ano = int(input('Qual ano você quer analisar? Digite 0 para analisar o ano atual: '))
if ano == 0: # SÓ PARA VALIDAR O VALOR 0
    ano = date.today().year
'''if ano % 100 == 0:
    bi = (ano % 400)
if ano % 100 != 0:
    bi = (ano % 4)'''
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))
