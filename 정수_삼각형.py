
import sys

n = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(len(arr[i])): #0 1
        if j == 0:
            arr[i][j] += arr[i-1][0]
        elif j == len(arr[i])-1:
            arr[i][j] += arr[i-1][-1]
        else:
            #print(max(arr[i-1][j-1], arr[i-1][j]))
            arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])

print(max(arr[-1]))


import sys

N, *lines = sys.stdin.read().rstrip().splitlines()
print(lines)