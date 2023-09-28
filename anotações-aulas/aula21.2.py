def par(n=0):
    if n % 2 == 0:
        return 'É par!'
    else:
        return 'Não é par!'


num = int(input('Digite um número: '))
print(par(num))
