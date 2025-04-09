
import sys
k = int(sys.stdin.readline().strip())

for _ in range(k):
    h, _, n = map(int, sys.stdin.readline().strip().split())
    '''
    if h == 1:
        i = str(1)
        j = str(n) ##이 케이스와
    '''
    #나누어 떨어짐(나누어 떨어지는 경우와 아닌 경우가 최초, 최대 분기점)
    if not n%h: 
        i = h ##이 케이스는 같은데 말이지
        j = n//h
 
    else:
        i = n%h
        j = n//h+1
    '''
    if len(j) == 1:
        j = str(0)+j
''' 
    print(i*100+j)  #print(i+j) 




'''
def solution(H, W, N):
    # 나머지가 0이면 해당 층의 마지막 방이므로 층수는 H
    if N % H == 0:
        floor = H
        room = N // H
    else:
        floor = N % H
        room = N // H + 1
    
    return floor * 100 + room ## 어차피 100의 자릿수이니까 100을 곱했어도 됐겠다

T = int(input())

for _ in range(T):
    H,W,N = map(int,input().split())
    print(solution(H,W,N))

'''
'''
import sys

# 프로그램은 표준 입력에서 입력 데이터를 받는다. 
# 프로그램의 입력은 T 개의 테스트 데이터로 이루어져 있는데 T 는 입력의 맨 첫 줄에 주어진다. 
# 각 테스트 데이터는 한 행으로서 H, W, N, 세 정수를 포함하고 있으며 
# 각각 호텔의 층 수, 각 층의 방 수, 몇 번째 손님인지를 나타낸다.
# (1 ≤ H, W ≤ 99, 1 ≤ N ≤ H × W).
    
# 출력 : 손님의 층수(H) + 호수(0~99사이이므로, 01호 , 02호 이런게 표현이 되어야함.)
T = int(input())
for i in range(T):
    H,W,n_customer = list(map(int,sys.stdin.readline().split()))
    floor = (n_customer%H)
    room_number = (n_customer//H)+1
    if floor == 0 :
        floor = H ## 아예 floor와 room_num을 먼저 고정해두고, 최고층일 경우 변경해주는 시스템
        room_number = room_number-1
    if room_number < 10:
        print(str(floor)+str(0)+str(room_number))
    else:
        print(str(floor)+str(room_number))
'''

import sys

readline = sys.stdin.readline
write = sys.stdout.write

for _ in range(int(input())):
    h, _, n = map(int, readline().split())
    write(f'{(n-1)%h + 1}{(n-1)//h + 1 :02d}\n')

