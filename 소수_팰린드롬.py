def strings(x):
    x = str(x)
    return x == x[::-1] #T/F를 출력하기에
'''
    x = str(x)
    if x == x[::-1]:
        return True
    else:
        return False
'''

def cal(x):
    if x <2:
        return False # 까먹는 부분(1도 팰린드롬수가 된다..!)
    
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            return False
    return True 


x = int(input())

while True:
    if strings(x): 
        if cal(x): # 최소 파츠 모듈로 만들어 놓기
            print(x)
            break
    x += 1


''' 
## strings에 cal을 안겨 두 조건문을 모두 평가할 필요가 없음ㅁ
while True:
    if strings(x) & cal(x):
        break
    else:
        x += 1
    
print(x)
'''

    
