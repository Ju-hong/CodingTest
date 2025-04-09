import sys

def GCD(a, b):
    while b:
        a, b= b, a%b
    return a


n = int(input())
list = list(map(int, sys.stdin.readline().strip().split()))
## [map]은 map object를 담는 list이고,
## list(map)는 map을 integer의 list로 변환


for i in range(1, n):
    gcd = GCD(list[0], list[i])
    print(int(list[0]//gcd), '/', int(list[i]//gcd), sep='')

