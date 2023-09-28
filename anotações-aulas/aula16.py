# TUPLAS EM PYTHON
lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim') #TUPLAS É (), LISTAS [], DICIONÁRIO {}
print('-'*20)
print('FATIAMENTO')
print('-'*20)
print(lanche[0])
print(lanche[-2])
print(lanche[1][0])
print('-'*20)
print('COMANDO FOR')
print('-'*20)
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
print('{:=^20}'.format('OU'))
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba!')
print('{:=^20}'.format('OU'))
for pos, comida in enumerate(lanche): #ENUMERATE DA O DADO E A POSIÇÃO
    print(f'Eu vou comer {comida} na posição {pos}')
print('-'*20)
print('COMANDO SORTED')
print('-'*20)
print(sorted(lanche)) #TRANSFORMA EM LISTA, VER O COLCHETE [] NO RUN
