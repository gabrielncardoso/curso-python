exp = str(input('Digite a expressão: '))
pilha = []
for l in exp:
    if l in '(':
        pilha.append(l)
    elif l in ')':
        if len(pilha) > 0:
            pilha.pop()
        else: #SE O LEN DA PILHA FOR = 0
            pilha.append(l)
            break
if len(pilha) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')
