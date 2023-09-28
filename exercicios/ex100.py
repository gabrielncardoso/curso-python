from time import sleep
from random import randint


def sorteia(a):
    print(f'Sorteando os {a} valores da lista: ', end='')
    for c in range(1, a+1):
        n = (randint(1, 10))
        numeros.append(n)
        print(n, end=' ')
        sleep(0.3)
    print('PRONTO!')


def somapar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {numeros}, temos {soma}!')


# PROGRAMA PRINCIPAL
numeros = []
qtd = int(input('Quantos números você quer sortear? '))
sorteia(qtd)
somapar(numeros)
