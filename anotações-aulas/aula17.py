num = [2, 5, 9, 1]
num[2] = 3
num.append((7))
num.sort(reverse=True)
num.insert(2, 2)
for n in num:
    if n == 2:
        num.remove(2)
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')
#num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
