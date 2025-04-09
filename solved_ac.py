
import sys

def rounding(n):
    if n - int(n) < 0.5:
        return int(n)
    else:
        return int(n) + 1

length = int(sys.stdin.readline().strip())

if length == 0:
    print(0)

else:
    n = rounding(length*0.15)
    temp = sorted([int(sys.stdin.readline().strip()) for _ in range(length)])
    k = temp[n:length-n] #length-n
    print(rounding(sum(k)/len(k)))

###########

import sys

def rounding(n):
    if n - int(n) < 0.5:
        return int(n)
    else:
        return int(n) + 1

length = int(sys.stdin.readline().strip())

if length == 0:
    print(0)

else:
    n = rounding(length*0.15)
    temp = [int(sys.stdin.readline().strip()) for _ in range(length)]
    temp.sort()
    
    k = temp[n:length-n] #length-n
    print(rounding(sum(k)/len(k)))

##########

import sys

n, *arr = map(int, sys.stdin.read().split()) # 이부분. split을 arr로 list로 et

if n == 0:
    sys.stdout.write('0')

else:
    arr.sort()
    cut = int(n * 0.15 + 0.5) # 자르는 갯수

    if cut > 0:
        arr = arr[cut:-cut] # 자른 리스트
        n -= 2 * cut
    sys.stdout.write(str(int(sum(arr) / n + 0.5)))