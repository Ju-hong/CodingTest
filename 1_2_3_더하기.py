import sys

n = int(sys.stdin.readline().rstrip())
list = list(map(int,sys.stdin.readlines()))


for i in list:
    dp = [1, 2, 4]
    if i <= 2:
        print(dp[i-1])
    else: 
        for j in range(i-3):
            dp[0], dp[1], dp[2] = dp[1], dp[2], dp[0] + dp[1] + dp[2]
        print(dp[-1])

