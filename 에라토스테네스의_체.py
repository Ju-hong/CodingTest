import sys

n, m = map(int, sys.stdin.readline().strip().split()) # 7 3

temp = [True]*(n+1)
count = 0

for i in range(2, n+1): #왜 여기는 sqrt가 아니지??

    for j in range(i, n+1, i):
        if temp[j] == True: 
            temp[j] = False
            count += 1
                
            if count == m:
                print(j)
                sys.exit ## 런타임에러가 나서 찾아봄

