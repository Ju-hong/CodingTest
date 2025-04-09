import sys

while True:
    
    temp = sorted(list(map(int, sys.stdin.readline().strip().split())))
    if sum(temp) == 0: #아, 논리 연산자가 아니라 sum으로도 가능
        break
    
    a, b, c = temp
        
    if c == 1:
        print("wrong")
    elif a**2 + b**2 == c**2:
        print("right")
    else:
        print("wrong")

   
    