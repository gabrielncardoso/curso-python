# CONVERSOR DE BASES
print('\033[1;33mBEM VINDO AO CONVERSOR DE BASES!\033[m')
n = int(input('Digite um número inteiro: '))
print('''Escolha qual será a base de conversão: 
\033[1;35m[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL\033[m''')
op = int(input('Digite a opção desejada: '))
if op == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(n, (bin(n)[2:])))
elif op == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n, (oct(n)[2:])))
elif op == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n, (hex(n)[2:])))
else:
    print('\033[1;31mOPÇÃO INVÁLIDA. TENTE NOVAMENTE\033[m')
