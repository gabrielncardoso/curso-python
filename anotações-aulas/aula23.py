try:
    n = int(input('Numerador: '))
    d = int(input('Denominador: '))
    r = n / d
except Exception as erro:
    print(f'Infelizmente tivemos um problema de {erro.__class__}:(')
else:
    print(f'O resultado é {r}')
finally:
    print('Obrigado pela preferência. Volte sempre!')
