from bisect import bisect_left, bisect_right
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().rstrip().split()))
dp = deque([arr[0]]) # 긴 수열 저장
len_arr = [1] # 길이 저장

for i in range(1, n):
    if arr[i] < dp[0]: # arr[i]가 현재 최소보다 작다
        dp.appendleft(arr[i]) # 내림차순
        len_arr.append(len_arr[-1]+1)
        #print(dp, len_arr)
        print(dp)
        
    else: # arr[i]가 현재 최소보다 작다
        idx = bisect_left(dp, arr[i])
        dp[idx-1] = arr[i]
        print(arr[i], idx, dp, arr)
        #print(idx, dp, len_arr)

print(len_arr[-1])




    

