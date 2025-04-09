import sys

length = sys.stdin.readline().strip()

temp = []

for _ in range(int(length)):
    num = list(map(int, sys.stdin.readline().strip().split()))
    
    if num[0] == 4:
        print(0) if temp else print(1)

    elif num[0] == 3:
        print(len(temp))
        
    elif num[0] == 2:
        print(temp.pop(-1)) if temp else print(-1)

    elif num[0] == 1:
        temp.append(num[1])

    elif num[0] == 5:
        print(temp[-1]) if temp else print(-1)
