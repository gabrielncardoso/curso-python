# ALISTAMENTO MILITAR
from datetime import date
s = str(input('Qual o seu sexo? ').lstrip())  # SEXO
if s[0] == 'M':
    an = int(input('Ano de nascimento: '))  # ANO NASCIMENTO
    aa = date.today().year  # ANO ATUAL
    i = aa - an  # IDADE
    print('Quem nasceu em {} faz {} anos em {}.'.format(an, i, aa))
    if i == 18:
        print('Você tem que se alistar \033[4mIMEDIATAMENTE\033[m!')
    elif i > 18:
        if (i - 18) == 1:
            print('''Você já deveria ter se alistado há {} anos.
Seu alistamento foi em {}!'''.format((i - 18), (an + 18)).replace('anos', 'ano'))
        else:
            print('''Você já deveria ter se alistado há {} anos.
Seu alistamento foi em {}!'''.format((i - 18), (an + 18)))
    elif i < 18:
        if (18 - i) == 1:
            print('''Ainda faltam {} anos para o seu alistamento.
Seu alistamento será em {}!'''.format((18 - i), (an + 18)).replace('anos', 'ano').replace('faltam', 'falta'))
        else:
            print('''Ainda faltam {} anos para o seu alistamento.
Seu alistamento será em {}!'''.format((18 - i), (an + 18)))
else:
    print('O alistamento militar não é obrigatório para você!')
