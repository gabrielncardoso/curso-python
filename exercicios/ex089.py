from time import sleep
alunos = []
lista = []
while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Nota 1: ')))
    lista.append(float(input('Nota 2: ')))
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    alunos.append(lista[:])
    lista.clear()
    if r in 'Nn':
        break
print('-=' * 20)
print(f'{"No.":<5}{"NOME":<15}{"MÉDIA":<10}')
print('-' * 30)
for i, a in enumerate(alunos):
    print(f'{i:<5}{a[0]:<15}{(a[1] + a[2])/2:<10}')
print('-' * 30)
while True:
    r = int(input('Mostrar a nota de qual aluno? (999 interrompe): '))
    if r != 999:
        print(f'Notas de {alunos[r][0]} são {alunos[r][1:]}')
    else:
        break
print('FINALIZANDO...')
sleep(1)
print('<<< VOLTE SEMPRE >>>')
