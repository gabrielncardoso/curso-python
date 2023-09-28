def escreva(msg):
    comp = (len(msg)+6)
    print('~' * comp)
    print(f'{msg:^{comp}}')
    print('~' * comp)


escreva('APRENDA PYTHON')
escreva('CURSO EM VÍDEO DO GUSTAVO GUANABARA')
escreva('Olá, Mundo!')
