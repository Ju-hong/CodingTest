import sys
from collections import deque

n = int(sys.stdin.readline().strip())
que = deque()

for _ in range(n):
    temp = sys.stdin.readline().strip().split()
    if temp[0] == "push":
        que.append(temp[1])

    elif temp[0] == "pop":
        if que:
            print(que.popleft())
        else:
            print(-1)

    elif temp[0] == "size":
        print(len(que))

    elif temp[0] == "empty":
        if que:
            print(0)
        else:
            print(1)

    elif temp[0] == "front":
        if que:
            print(que[0])
        else:
            print(-1)

    elif temp[0] == "back":
        if not que:
            print(-1)
        else:
            print(que[-1]) ###

