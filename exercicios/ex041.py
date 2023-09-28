#CLASSIFICANDO ATLETAS
from datetime import date
an = int(input('Ano de nascimento: '))
aa = date.today().year
i = aa - an
print('O atleta nascido em {} tem {} anos.'.format(an, i))
if i <= 9:
    print('CLASSIFICAÇÃO: MIRIM')
elif i <= 14:
    print('CLASSIFICAÇÃO: INFANTIL')
elif i <= 19:
    print('CLASSIFICAÇÃO: JÚNIOR')
elif i <= 25:
    print('CLASSIFICAÇÃO: SÊNIOR')
elif i > 25:
    print('CLASSIFICAÇÃO: MASTER')
