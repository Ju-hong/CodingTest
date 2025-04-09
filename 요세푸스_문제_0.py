from collections import deque

n, m = map(int, input().split()) # 7 3

temp = deque([i for i in range(1, n+1)]) # 1~7
final = []

print("<", end="")

while True:
    temp.rotate(-m+1)
    print(temp.popleft(), end = "")
    if temp:
        print(", ", end = "")
    else:
        print(">")
        break
##print("<" + ", ".join(str(num) for num in Josephus) + ">")
