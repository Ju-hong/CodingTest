import sys

n, m = map(int, sys.stdin.readline().strip().split())

a = max(map(int, sys.stdin.readline().strip().split()))
b = max(map(int, sys.stdin.readline().strip().split()))
print(a+b)