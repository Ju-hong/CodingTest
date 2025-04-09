
## from bisect import bisect_left #out of range일 경우 맨 끝 위치 출력
## dp를 이용해 풀어야 함

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

dp = [1]*n

for i in range(1, n):  # temp[2]
    for j in range(0, i): # temp[0], temp[1]
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

max_i = max(dp)
print(max(dp))

result = []

for i in range(n-1, -1, -1):
    if dp[i] == max_i :
        result.append(arr[i])
        max_i -= 1


print(*sorted(result))
# result max를 변경하는 경우에만 bisect_left






n = int(input()) # 수열의 길이
a = list(map(int, input().split())) # 수열
dp = [[a[i]] for i in range(n)] # dp, 초기 수열 설정
# print(dp)

for i in range(1, len(a)) :
    num = a[i]
    for j in range(0, i) :
        if a[j] < num and len(dp[i]) <= len(dp[j]): # 증가하는 수열인지 and 최장증가수열인지
            dp[i] = dp[j] + [num]

answer = max(dp, key = len)
print(len(answer))
print(* answer)
