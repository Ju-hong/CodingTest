temp = []

for _ in range(int(input())):
    num = int(input())
    if num:
        temp.append(num)
    else:
        temp.pop()

print(sum(temp))


