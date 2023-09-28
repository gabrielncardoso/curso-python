def mensagem(msg):
    print('-' * 30)
    print(f'{msg:^30}')
    print('-' * 30)
def soma(a, b):
    s = a + b
    print(s)
def soma2(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


# PROGRAMA PRINCIPAL (precisa ter duas linhas abaixo do def)
mensagem('CURSO EM VÍDEO')
mensagem('APRENDA PYTHON')
soma(2, 5)
soma2(b=3, a=8)
