import re

N, M = map(int, input().split())

lines = (list(input() for i in range(N)))

mystring = "".join(lines[j][i] for i in range(M) for j in range(N))
cleanedStr = re.sub(r"(?<=\w)(\W+)(?=\w)", r" ", mystring)
print(cleanedStr)
