import sys

def gcd(a, b):
    ori_a = a
    ori_b = b
    while True:
        if b % a:
            b, a = a, b%a
        else:
            return ori_a*ori_b//a

n = int(sys.stdin.readline().strip())

for _ in range(n):
    a, b = map(int, sys.stdin.readline().strip().split())
    print(gcd(a, b))