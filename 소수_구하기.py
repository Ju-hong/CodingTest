
## 손코딩 해보기
import sys

def calcul(x):
    n, m = map(int, x.split())
    
    for i in range(n, m+1): # 3 16
        
        if i == 1:
            continue
        
        for j in range(2, int(i**0.5)+1):

            if i % j == 0:
                break
                
        else:
            print(i)


calcul(sys.stdin.readline().strip())


'''
def calcul(x):
    n, m = map(int, x.split())
    
    for i in range(n, m+1): # 3 16
                
        for j in range(2, int(i**0.5)+1):

            if i % j == 0:
                break 
            # 내부 break 종료 후 print(4 실행)
            # break는 가장 안쪽 루프만 종료되므로 그 다음 print(i)는 그대로
        
        print(i)


calcul(sys.stdin.readline().strip())
'''