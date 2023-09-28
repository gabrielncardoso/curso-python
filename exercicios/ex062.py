print('Gerador de PA')
print('-='*10)
n1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = 0
mais = 1
while termo < 10:
    print(n1, '-> ', end='')
    n1 += r
    termo += 1
print('PAUSA')
while mais != 0:
    mais = int(input('Quantos termos você quer mostrar a mais? '))
    contadortn = 0
    while contadortn < termonovo:
        print(n1, '-> ', end='')
        n1 += r
        termo += 1
        contadortn += 1
print('Progressão finalizada com {} termos'.format(termo))
