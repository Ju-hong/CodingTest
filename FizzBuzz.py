import sys

def number(a):
    if a % 15 ==0 :
        return "FizzBuzz"
    elif a%5 == 0:
        return "Buzz"
    elif a%3 == 0:
        return "Fizz"
    else:
        return a

temp = [sys.stdin.readline().strip() for _ in range(3)]

for i in temp:
    try: # 나는 string에는 int에 type error가 나타남을 이용
        int(i)
        x = (3 - temp.index(i)) + int(i)
        print(number(x))
        break
    except:
        pass

'''
#1
for i in range(3, 0, -1): # input이 3개로 제한
    x = input()
    if x not in ['Fizz', 'Buzz', 'FizzBuzz']:
        n = int(x) + i 
        # 1번이 숫자이면 +3
        # 2번이 숫자이면 +2... 이런 순서로 1까지
        # 그래서 n을 출력하고
        break
        
print('Fizz'*(n % 3 == 0) + 'Buzz'*(n % 5 == 0) or n)
# 논리 연산자로 T/F를 string에 곱해
# 두 가지를 만족하면 string plus(문자열)



#2
for i in range(3):
    s = input()
    if s not in ['Fizz', 'Buzz', 'FizzBuzz']:
        n = int(s)+3-i
'''