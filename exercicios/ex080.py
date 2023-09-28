numeros = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > numeros[-1]: # ADICIONA O NUMERO NO FINAL DA LISTA, CASO ELE SEJA O PRIMEIRO DIGITADO OU SEJA MAIOR QUE O ÚLTIMO DA LISTA
        numeros.append(n)
        print('Adicionado ao final da lista!')
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                print(f'Adicionado à posição {pos} da lista!')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {numeros}')
