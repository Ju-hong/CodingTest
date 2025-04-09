
import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

len_a = len(a)+1
len_b = len(b)+1

dp = [[0 for _ in range(len_a)] for _ in range(len_b)]


for j in range(1, len_b):
    for i in range(1, len_a):
        if a[i-1] == b[j-1]:
            dp[j][i] = dp[j - 1][i - 1] + 1 # 여기가 차이!
        else:
            dp[j][i] = max(dp[j-1][i], dp[j][i-1])

print(dp)     
print(max(dp[-1]))


############


def main():
    import sys

    word1 = sys.stdin.readline().rstrip()
    word2 = sys.stdin.readline().rstrip()

    l1 = len(word1)
    l2 = len(word2)

    dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
    
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j-1] + 1)
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    print(dp)
    sys.stdout.write(str(dp[-1][-1]))


if __name__ == '__main__':
    main()