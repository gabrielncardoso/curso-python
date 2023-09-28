from time import sleep

def maior(* num):
    mai = 0
    print('-=' * 30)
    print('Analisando os valores recebidos...')
    for n in num:
        print(n, end=' ')
        sleep(0.3)
        if n > mai:
            mai = n
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {mai}.')


#PROGRAMA PRINCIPAL
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
