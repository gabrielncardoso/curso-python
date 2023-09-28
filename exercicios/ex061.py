print('Gerador de PA')
print('=-='*10)
n1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c = 0
while c < 10:
    print(n1, end=' -> ')
    n1 += r
    c += 1
print('FIM')
