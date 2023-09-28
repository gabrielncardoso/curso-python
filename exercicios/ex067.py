while True:
    termo = 1
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    print('-'*30)
    while True:
        print(f'{num} x {termo} = {num*termo}')
        termo += 1
        if termo == 11:
            break
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO! Volte sempre')
