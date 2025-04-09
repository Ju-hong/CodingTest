
goal = int(input()) #인풋받은 goal 고정
num = goal # 변경해줄 num 설정
cnt = 0

while True:
    num1 = num // 10
    num2 = num % 10
    num = num2*10 + (num1 + num2)%10 
    cnt += 1

    if goal == num: 
        break

    # 필수 단계
    # 1) 입력 받은 수로 새로운 수 만들기(1의 자리)
    # 2) 이어붙인 수 만들기(10의 자리)

    # while로 조건을 만들려고 했는데, if로 받는게 더 간단함(순서적으로도)
    # 왜냐하면 1번은 저 조건을 돌려야 하거든
    
print(cnt)






'''
# str[0] str[1]을
# int로 바꿔 합하고
# str[1]과 str(int) 병합
def func(x):
    
    goal = x
    count = 0

    while True:
        if x == '0':
            return 1
        
        if len(x) == 1:
            n = '0'
            m = x
        else:
            n, m = x[0], x[1]
            
        # k는 str(sum(map(int, ['0', '1'])))이므로 '1’
        k = str(sum(map(int, [n, m])))
        x = m + k[-1] #x는 m + k[-1]이므로 ‘1’ + ‘1’ = '11’
        count += 1

        if x == goal:
            return count

print(func(input()))
# https://yoonsang-it.tistory.com/6#:~:text=%EB%A8%BC%EC%A0%80%20%EC%A3%BC%EC%96%B4%EC%A7%84%20%EC%88%98%EA%B0%80%2010%EB%B3%B4%EB%8B%A4%20%EC%9E%91%EB%8B%A4%EB%A9%B4%20%EC%95%9E%EC%97%90%200%EC%9D%84%20%EB%B6%99%EC%97%AC,%3D%208%EC%9D%B4%EB%8B%A4.%20%EC%83%88%EB%A1%9C%EC%9A%B4%20%EC%88%98%EB%8A%94%2068%EC%9D%B4%EB%8B%A4.%206%2B8%20%3D%2014%EC%9D%B4%EB%8B%A4.
'''