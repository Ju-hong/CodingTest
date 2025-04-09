'''
import sys

n = int(sys.stdin.readline().strip())

temp = [int(num.strip()) for num in sys.stdin.readlines()]

for num1 in range(n):
    floor = temp[2*num1]    #i층
    number = temp[2*num1+1] #j호
    zero = [k for k in range(1, number+1)] #0층

    for num2 in range(floor): # 1
        new = []
        for num3 in range(number): # 3
            new.append(sum(zero[:num3+1]))
        zero = new
    
    print(zero[-1])
'''
########
n = int(input())

for num1 in range(n):
    floor = int(input())   # 왜 굳이 저렇게 어렵게 받았지 ㅋㅋ
    number = int(input())  
    zero = [k for k in range(1, number+1)] #0층

    for num2 in range(floor): 
        for num3 in range(1, number):
            zero[num3] += zero[num3-1]
    
    print(zero[-1])



'''
#########

t = int(input())

for _ in range(t):  
    floor = int(input())  # 1층
    num = int(input())  # 3호
    f0 = [x for x in range(1, num+1)]  # 0층 리스트
    
    # 층 수 만큼 반복 (1, 2)
    for k in range(floor):  
        # 1 ~ n-1까지 (인덱스로 사용)
        for i in range(1, num): 
            # 층별 각 호실의 사람 수를 변경
            f0[i] += f0[i-1] 
            # 현 호수의 전 호수는, 항상 이전 호수까지 아랫층 인원수와 같다.
            # 따라서 바로 아랫 호수와 전 호수 사람을 합 = 현재 호수 사람 수

    print(f0[-1])  # 가장 마지막 수 출력


# 2: 1 4 10 20
# 1: 1 3 6  10 
# 0: 1 2 3  4
'''
