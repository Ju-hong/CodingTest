
import sys

num = int(input())

for i in range(num):
    a = sys.stdin.readline().strip().split()
    print(f'Case #{i+1}: {' '.join(a[::-1])}')
