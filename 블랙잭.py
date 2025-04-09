import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

arr = list(map(int, sys.stdin.readline().rstrip().split()))
maxi = []

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            a = arr[i] + arr[j] + arr[k]
            if a <= m:
                maxi.append(a)
print(max(maxi))

#####
import sys
input = sys.stdin.readline

def main():
    n, m = map(int,input().split())
    # n장의 카드 m을 넘지 않고 m에 가까운 3장 고르기
    cardList = list(map(int,input().split()))
    ans = 2
    
    for i in range(n-2):
        for j in range(i+1, n-1):
            for l in range(j+1, n):
                summ = cardList[i]+cardList[j]+cardList[l]
                
                if summ == m:
                    print(summ)
                    return 0
                else:
                    if summ < m and ans < summ:
                        ans = summ
    print(ans)

if __name__ == "__main__":
    main()
