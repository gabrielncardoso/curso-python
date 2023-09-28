from random import randint
contadorvit = 0
print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
while True:
    print('=-' * 15)
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    soma = jogador + computador
    tipo = ' '
    while tipo not in 'PI': #VALIDA A INFORMAÇÃO, SÓ PASSA PRA FRENTE ENQUANTO FOR PAR OU ÍMPAR
        tipo = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    resultado = 'PAR' if soma % 2 == 0 else 'ÍMPAR'
    print('-'*30)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} deu {resultado}')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!')
            contadorvit += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if soma % 1 == 1:
            print('Você VENCEU!')
            contadorvit += 1
        else:
            print('Você PERDEU!')
            break
    print('-' * 30)
    print('Vamos jogar novamente...')
    print('=-'*15)
print(f'GAME OVER! Você venceu {contadorvit} vezes.')

