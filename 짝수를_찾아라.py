num = int(input())

for _ in range(num):
    temp = map(int, input().split())
    num2 = 0
    temp2= []
    for j in temp:
        if j%2 == 0:
            temp2.append(j)
            num2 += j
    print(num2, min(temp2))