import sys

n = int(sys.stdin.readline().strip())

for _ in range(n):
    temp = sys.stdin.readline().strip().split("X")
    number = 0
    for word in temp: #00
        count = 0
        for i in word:
            number = number + 1 + count
            count += 1
    print(number)


'''
n=int(input())

for _ in range(n):
    temp=list(input())
    number, count=0,1 # number와 count는 총 5번 0이 됨

    for i in temp: #00
        if i =='O': # O가 지속되면 여기서 돈다
            number+=count 
            count+=1
        else:
            count=1 #X가 나오면 바로 여기로

    print(number)
'''

'''
t = int(input())

for _ in range(t):
    score = 0

    result = input().split("X") #00,'' , 000, 0
    result = [s for s in result if s] # 

    for Os in result:
        score += len(Os)*(len(Os)+1)//2

    print(score

'''


'''
import sys, re

n = int(sys.stdin.readline().strip())

for _ in range(n):
    temp = re.split(r"X+", sys.stdin.readline().strip())
    number = 0
    for word in temp: #00
        count = 0
        for i in word:
            number = number +1 +count
            count += 1
    print(number)


'''

        



