try:
    n = int(input('Numerador: '))
    d = int(input('Denominador: '))
    r = n / d
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Obrigado pela preferência. Volte sempre!')
