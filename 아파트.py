
import sys
from collections import deque

_ = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())
queing = deque(map(int, sys.stdin.readline().strip().split()))
count =  list(map(int, sys.stdin.readline().strip().split()))

for i in range(n):
    queing.rotate(-(count[i])+1)
    print(queing[0], end=" ")

#############  

import sys 

_ = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())
queing = list(map(int, sys.stdin.readline().strip().split()))
count =  list(map(int, sys.stdin.readline().strip().split()))

num = 0

for i in range(n):
    num = num + count[i] - 1
    if num >= len(queing):
        num = num % len(queing) # num = (num + count[i] - 1) % len(queing)
    print(queing[num], end=" ")

#############  

import sys
input = sys.stdin.readline

N = int(input())
T = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
loser = []

i = 0

for j in range(T):
    # 가장 아래 있던 손에서 시작(or not i+1)
    i = (i + b[j] - 1) % len(a) 
    #현재 위치 + 더한 위치, 서수-1 = index값
    # 나머지값은 몇이 남든 그 위치 정보를 보존함
    loser.append(a[i])
print(*loser, sep=' ')


#############  

N = int(input())
T = int(input())
stack = list(map(int,input().split()))
temp = list(map(int,input().split()))
pos = -1

for i in range(T):
    pos += temp[i]
    pos %= 2*N # = len(temp)
    print(stack[pos],end=" ")
    pos -=1

#############  

#백준 32979 아파트
N=int(input()) # 4
T=int(input()) # 2
pos=list(map(int,input().split())) # 2 4 4 3 3 1 2 1
num=list(map(int,input().split())) # 3 12 
 
for i in range(T):
    num[i]=num[i]%(2*N) #num%len(pos)
    if num[i]==0:
        print(pos[2*N-1],end=' ') # 0이면 -1번 위치
        pos.insert(0,pos.pop()) # 멘 뒤 것을 빼서 맨 앞으로
    else:
        print(pos[num[i]-1],end=' ')
        pos=pos[num[i]-1:2*N]+pos[0:num[i]-1] #list 재정렬:끝위치~끝 + 시작~끝위치(deq.rotate)
