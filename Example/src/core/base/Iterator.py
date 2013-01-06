from itertools import count, cycle, repeat, chain

# count(start = 0, step = 1)
for i in count(100, 2):   # 100 102 104 -> ...
    break

for c in cycle('ABCDEFG'):    # A B C D E F G A B -> ...
    break

# repeat(element, [n])
for c in repeat('10', 3):
    break

# chain(iter1, iter2, ...)
for e in chain(repeat(10, 3), repeat(11, 3)):
    print e, 