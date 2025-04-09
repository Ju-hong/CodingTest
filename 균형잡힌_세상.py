import sys
from collections import deque

def sentence(words):
    words = words.replace(" ", "")

    num1 = 0
    num2 = 0
    temp = deque([])

    for i in words:
        if i in "()[]":
            if i == "[":
                num1 += 1
                temp.appendleft("[")
            elif i == "(":
                num2 += 1
                temp.appendleft("(")


            elif i == "]":
                num1 -= 1
                if (num1 < 0) or (temp[0] != "["):
                    return "no"
                else:
                    temp.popleft()                  
            elif i == ")":
                num2 -= 1
                if (num2 < 0) or (temp[0] != "("):
                    return "no"
                else:
                    temp.popleft()           

        elif i == ".":
            if (num1 > 0) or (num2 > 0):
                return "no"
            else:
                return "yes"

while True:
    a = sys.stdin.readline().rstrip()
    if a == ".":
        break
    print(sentence(a))

###########

import sys

def is_balanced(sentence):
    stack = []
    for char in sentence:
        if char == '(' or char == '[': # if char in "([":
            stack.append(char)

        elif char == ')':
            if not stack or stack[-1] != '(':
                return "no"
            stack.pop()

        elif char == ']':
            if not stack or stack[-1] != '[':
                return "no"
            stack.pop()
            
    return "yes" if not stack else "no"

# 입력 처리
while True:
    line = sys.stdin.readline().rstrip()  # 개행 문자 제거
    if line == ".":  # 종료 조건
        break
    print(is_balanced(line))


###########  

import sys

lines = []
while True:
    line = sys.stdin.readline().rstrip()
    if line == '.': # '.'는 건너뜀
        break ##

    stack = []
    failed = False

    for cha in line:
        if cha in ('(', '['):
            stack.append(cha)

        elif cha == ')':
            # and 조건문이기 때문에 스택이 비어 있지 않은지 확인합니다 (if stack)
            # 그런 다음 스택의 맨 위 요소가 '('인지 확인합니다 (stack[-1] == '(')
            # stack = True를 확인하지 않으면
            # 스택이 비어 있을 경우, stack[-1]에 접근하려고 하면 IndexError가 발생할 수 있습니다. 
            # 하지만 이 조건문은 스택이 비어 있는지 먼저 확인하기 때문에 안전합니다.
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                failed = True
                break ####

        elif cha == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                failed = True
                break ####

    if failed or stack:
        sys.stdout.write('no\n') ###
    else:
        sys.stdout.write('yes\n') ###
