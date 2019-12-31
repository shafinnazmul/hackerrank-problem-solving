from itertools import groupby

x = groupby(input())
ls1 = [(len(list(c)), int(k)) for k, c in x]
print(*ls1)
