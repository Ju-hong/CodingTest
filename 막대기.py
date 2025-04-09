import sys

num = int(sys.stdin.readline().strip())
numlist = [int(sys.stdin.readline().strip()) for _ in range(num)]
count = 0
maxnum = 0
# print(numlist)

for i in range(len(numlist)):
    if numlist[-1-i] > maxnum:
        maxnum = numlist[-i-1]
        count += 1

print(count)
