import sys

def cal(n, m): #내가 짰지만 구조가 살짝 헷갈림
    while True:
        if n < m:
            n, m = m, n

        if n % m:
            n, m = m, n%m
        else:
            return m

count = int(sys.stdin.readline().strip())

for _ in range(count):
    n, m = map(int, sys.stdin.readline().strip().split())
    print(cal(n,m))