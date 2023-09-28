matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = mai = s3coluna = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para a posição [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
        if matriz[l][c] % 2 == 0:
            somapares += matriz[l][c] #COMO JA TA VARRENDO TODOS OS NUMEROS, DA PRA APROVEITAR E FAZER A SOMA DOS PARES
    print() #PULA A LINHA NO FINAL DE CADA LINHA
print('-=' * 30)
for l in range(0, 3):
    s3coluna += matriz[l][2]
for n in matriz[1]: #MAIOR DA SEGUNDA LINHA
    if n > mai:
        mai = n
print(f'A soma dos valores pares é {somapares}.')
print(f'A soma dos valores da terceira coluna é {s3coluna}.')
print(f'O maior valor da segunda linha é {mai}.')
