import sys

n = int(sys.stdin.readline().strip())

temp = [0]*10001

for _ in range(n): # [0, 2, 2, 2, 1, 2, 0, 1, 
    temp[int(sys.stdin.readline().strip())] += 1

for i in range(1, len(temp)):
    if temp[i] != 0:
        for _ in range(temp[i]):
            print(i)

######

import sys

n = int(sys.stdin.readline().rstrip())
counter = [0 for _ in range(10000)]

for _ in range(n):
    counter[int(sys.stdin.readline().rstrip()) - 1] += 1

for i in range(10000):
    count = counter[i]
    for _ in range(count):
        sys.stdout.write(str(i+1) + '\n')