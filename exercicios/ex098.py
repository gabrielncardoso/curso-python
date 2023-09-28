from time import sleep
def contar(i, f, p):
    if i < f and p > 0:
        print('-=' * 30)
        print(f'Contagem de {i} até {f} de {p} em {p}')
        for c in range(i, f+1, p):
            print(c, end=' ')
            sleep(0.2)
        print('FIM!')
    if i > f:
        if p > 0:
            print('-=' * 30)
            print(f'Contagem de {i} até {f} de {p} em {p}')
            for c in range(i, f-1, -p):
                print(c, end=' ')
                sleep(0.2)
            print('FIM!')
        if p < 0:
            print('-=' * 30)
            print(f'Contagem de {i} até {f} de {-p} em {-p}')
            for c in range(i, f - 1, p):
                print(c, end=' ')
                sleep(0.1)
            print('FIM!')


#PROGRAMA PRINCIPAL
contar(1, 10, 1)
contar(10, 0, 2)
print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contar(ini, fim, pas)
