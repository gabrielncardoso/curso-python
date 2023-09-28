# CRIANDO UM MENU DE OPÇÕES
from time import sleep
pv = int(input('Primeiro valor: '))
sv = int(input('Segundo valor: '))
op = 0
if pv > sv:
    mv = pv
elif sv > pv:
    mv = sv
while op != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    op = int(input('>>>>> Digite a opção desejada: '))
    if op == 1:
        soma = pv + sv
        print('A soma entre {} + {} é {}'.format(pv, sv, soma))
        print('=-='*10)
    elif op == 2:
        mult = pv * sv
        print('A operação {} x {} é {}'.format(pv, sv, mult))
        print('=-=' * 10)
    elif op == 3:
        if pv != sv:
            print('Entre {} e {}, o maior valor e {}'.format(pv, sv, mv))
            print('=-=' * 10)
        else:
            print('Os valores são iguais!')
            print('=-=' * 10)
    elif op == 4:
        print('Informe os números novamente...')
        pv = int(input('Primeiro Valor: '))
        sv = int(input('Segundo Valor: '))
    elif op == 5:
        print('Finalizando...')
        print('=-=' * 10)
    else:
        print('Opção inválida. Tente novamente.')
        print('=-=' * 10)
    sleep(1)
print('Fim do programa. Volte sempre!')