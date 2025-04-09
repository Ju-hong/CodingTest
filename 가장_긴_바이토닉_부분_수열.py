import sys
def dp_increasing(arr, n):
    dp = [1 for _ in range(n)]

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return dp, arr

def dp_decreasing(arr, n):
    dp = [1 for _ in range(n)]
    arr = list(reversed(arr))
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return dp, arr

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))


for j in range(1, n):
        
        a = max(increasing_len_arr[:j]) + max(decreasing_len_arr[:n-j])
            
        if increasing_arr[j] == decreasing_arr[j]:
            if increasing_arr[:j:-1] == decreasing_arr[:j]:
                a = a
            else:
                a -= 1
        temp.append(a)

    print(max(temp))

















'''
def dp_increasing(arr, n):
    dp = [1 for _ in range(n)]

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return dp, arr

def dp_decreasing(arr, n):
    dp = [1 for _ in range(n)]
    arr = list(reversed(arr))
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return dp, arr

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

increasing_len_arr, increasing_arr = dp_increasing(arr, n)
decreasing_len_arr, decreasing_arr = dp_decreasing(arr, n)

#print(dp_increasing(arr, n), dp_decreasing(arr, n))
# print(increasing_arr, decreasing_arr)

temp = []

if n == 1:
    print(1)
else:
    for j in range(1, n):
        
        a = max(increasing_len_arr[:j]) + max(decreasing_len_arr[:n-j])
            
        if increasing_arr[j] == decreasing_arr[j]:
            if increasing_arr[:j:-1] == decreasing_arr[:j]:
                a = a
            else:
                a -= 1
        temp.append(a)

    print(max(temp))

# https://www.acmicpc.net/board/view/56223
#3, 18

'''



