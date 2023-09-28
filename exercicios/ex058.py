from random import randint
nc = randint(1, 10)
print('Sou seu computador...\n'
      'Acabei de pensar em um número entre 0 e 10\n'
      'Será que você consegue adivinhar qual foi?')
p = 0
t = 1
p = int(input('Qual é o seu palpite? '))
while p != nc:
    if p > nc:
        p = int(input('Menos... Tente novamente: '))
        t += 1
    if p < nc:
        p = int(input('Mais... Tente novamente: '))
        t += 1
if t == 1:
    print('Acertou com {} tentativa. Parabéns!'.format(t))
else:
    print('Acertou com {} tentativas. Parabéns!'.format(t))
