print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for c in range(t, t+(10*r), r):
    print(c, end=' -> ')
print('ACABOU')
