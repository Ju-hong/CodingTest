import sys

def fibo(n):
    arr = [0, 1, 1]

    if n == 0:
        return 1, arr[n]

    elif n == 1:
        return 0, arr[n]   
    
    else:
        for _ in range(3, n+1):
            arr[0], arr[1], arr[2] = arr[1], arr[2], arr[1]+arr[2]
    
    return arr[1], arr[2]

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    print(' '.join(map(str, fibo(num))))


# 1의 출력은 n번째 숫자이고
# 0은 n-1번째 숫자와 같다.












'''
class fibonacci:
    def __init__(self, n):
        self.n = int(n)
        self.zero = 0
    
    def fibo(self, n):
        if n == 0:
            self.zero += 1
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibo(n-1) + self.fibo(n-2)

    def counting(self):
        return self.zero


n = int(input())

for _ in range(n):
    a = int(input())
    f = fibonacci(a) #a를 넣고 __init__
    fibo_one = f.fibo(a)
    fibo_zero =f.counting()
    print(fibo_zero, fibo_one)

'''
