import sys

temp = []

for _ in range(5):
    num = int(sys.stdin.readline().strip())
    if num < 40:
        num = 40
    temp.append(num)

print(int(sum(temp)/5))


