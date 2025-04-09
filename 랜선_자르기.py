import sys

n, m = map(int, sys.stdin.readline().strip().split())

n, m = map(int, sys.stdin.readline().strip().split())






'''
import sys

n, m = map(int, sys.stdin.readline().strip().split())

temp = [int(sys.stdin.readline().strip()) for _ in range(n)]

for k in range(max(temp), 0, -1):
    # 숫자 내에서 반복
    if m <= sum(i//k for i in temp): # 각 원소를 같은 같으로 나눈 몫의 합
        print(k)
        break
'''