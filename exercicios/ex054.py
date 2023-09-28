from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}a pessoa nasceu? '.format(c)))
    if atual - ano >= 18:
        maior += 1
    else:
        menor += 1
print('Ao todo, tivemos {} alunos maiores de idade \nE também tivemos {} menores de idade!'.format(maior, menor))
