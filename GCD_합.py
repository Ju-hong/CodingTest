import sys








'''
def gcd(a, b):
    if a < b:
        a, b = b, a

    while b:
        a, b = b, a%b

    return a

n = int(sys.stdin.readline().strip())

for _ in range(n):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    print(sum(gcd(temp[i], temp[j]) 
              for i in range(1, len(temp)-1) 
              for j in range(i+1, len(temp))))

'''