import sys
n = int(sys.stdin.readline().strip())

temp = list(map(int, sys.stdin.readline().strip().split()))

dp = [1]*n


for i in range(1, n): # temp[2]
    for j in range(0, i): # temp[0], temp[1]
        if temp[j] < temp[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
    

 # 시작 ~ 임시끝점-1까지
 # 현재 임시끝점 값이 임시끝점까지보다 크면
 # len + 1
###

'''
 import sys
n = int(sys.stdin.readline().strip())
temp = list(map(int, sys.stdin.readline().strip().split()))

dp = [1]*n


for i in range(0, n):
    if i == 0:
        dp[i] = 1
    elif temp[i] > max(temp[:i]):
        dp[i] = max(dp) + 1
    else:
        dp[i] = dp[i]

print(max(dp))
 
'''
