a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(sorted(a))
print(sorted(b))
print(c)
c = b + a # EM TUPLAS, É DIFERENTE DE A + B
print(c)
print(sorted(c))
print(len(c))
print(c.count(5))
print(c.index(1))
print(c.index(5, 1))
