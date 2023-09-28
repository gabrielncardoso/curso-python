#MÉDIA DO ALUNO
from time import sleep
print('\033[1;35mCALCULADORA DE MÉDIA\033[m')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print('\033[1;35mPROCESSANDO...\033[m')
sleep(2)
print('Tirando {:.1f} e {:.1f}, a média final do aluno é {:.1f}!'.format(n1, n2, m))
if m < 5:
    print('\033[1;31mO ALUNO ESTÁ REPROVADO.\033[m')
elif 5 <= m < 7.0:
    print('\033[1;33mO ALUNO ESTÁ EM RECUPERAÇÃO.\033[m')
elif m >= 7:
    print('\033[1;32mO ALUNO ESTÁ APROVADO.\033[m')
