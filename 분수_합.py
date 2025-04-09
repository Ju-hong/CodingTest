'''
def GCD(x, y):
    if x < y:
        x, y = y, x
    
    while True:
        if x % y == 0:
            return y
        else:
            x, y = y, x%y # 바로 생각나게 연습


def gcd(a, b):
    while a % b != 0:
        mod = a % b
        a = b
        b = mod
    return b  ## return의 위치에 유의
'''
def GCD(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1


i, j = map(int, input().split())
n, m = map(int, input().split())

gcd = GCD(j, m)
lcd = j*m//gcd # 최소공배수

sumi = i * (lcd//j) + n * (lcd//m) # 31
mol = (i * m//gcd) + (n * j//gcd)
# 알반적으로 두 분수의 공통 분모는 두 분모를 곱해서 만든다
# 이때, 분자와 분모에 같은 타 분모를 곱하게 된다
# 분모를 최소공배수로 맞출 때, 최대공약수로 나누기도 분모 분자에 공평하게

gcd2 = GCD(sumi, lcd) # 31 35 공약수

print(int(sumi/gcd2), int(lcd/gcd2))

