
# n-1, n-2번째 수 합이 n번째 수인 수열에서 n번째 값은?
# 이전 값들에 현재 값이 영향을 받는 수열
def fibo1(n):
    global count1 
    if n == 1 or n ==2 :
        return 1
    else:
        return fibo1(n-1) + fibo1(n-2)


def fibo2(n):
    count2= 0
    f = [0]*(n+1) # index 어렵다
    f[1], f[2] = 1, 1

    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2] 
        count2 += 1
    return count2


n = int(input())


print(fibo1(n), fibo2(n))

######

def fibo_dp(n):
    dp_table = [1] * n
    cnt = 0
    for i in range(2, n):
        cnt +=1
        dp_table[i] = dp_table[i-1] + dp_table[i-2]
    return dp_table[n-1], cnt

n = int(input())

ans_1, ans_2 = fibo_dp(n)

print(ans_1, ans_2)

######

def main():
    import sys
    
    n = int(sys.stdin.readline())
    dp = [0, 1, 1]
    for _ in range(3, n + 1):
        dp[0], dp[1], dp[2] = dp[1], dp[2], dp[1] + dp[2]
    
    sys.stdout.write(f'{dp[2]} {n - 2}')

if __name__ == '__main__':
    main()