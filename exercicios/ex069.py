tot18 = totH = totM20 = 0
while True:
    sexo = ' '
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade: '))
    while sexo not in 'MF': #VALIDAR O SEXO, SÓ PASSA SE A RESPOSTA FOR M OU F
        sexo = str(input('Sexo: [M/F]')).upper().strip()[0]
    if idade > 18:
        tot18 += 1
    if sexo in 'M':
        totH += 1
    if sexo in 'F' and idade < 20:
        totM20 += 1
    print('-'*20)
    seguir = ' '
    while seguir not in 'SN':
        seguir = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if seguir == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}.')
print(f'Ao todo temos {totH} homem(s) cadastrado(s)')
print(f'E temos {totM20} mulheres com menos de 20 anos.')
