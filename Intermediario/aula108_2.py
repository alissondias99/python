# count - iterador sem fim

from itertools import count

c1 = count(2, 3) # começo e passo
r1 = range(2, 10, 3) # começo, fim e passo

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))

print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))

print('count')
for i in c1:
    if i >= 10:
        break
    print(i)   
print()

print('range')
for i in r1:
    print(i)