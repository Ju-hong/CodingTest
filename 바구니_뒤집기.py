import sys

n, m = map(int, sys.stdin.readline().split())

temp = [str(_) for _ in range(1, n+1)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    if i != j:
        temp[i-1:j] = temp[i-1:j][::-1]
        
print(' '.join((temp)))
