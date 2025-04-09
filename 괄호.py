import sys

num = int(input())

for _ in range(num):
    count = 0
    temp = list(sys.stdin.readline().strip())
    for i in temp:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        if count < 0: ## 여기가 핵심
            break
    
    if count == 0 :
        print('YES')
    else:
        print('NO')
        
