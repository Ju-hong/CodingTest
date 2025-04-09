n = int(input())
temp = [i for i in input()]
listi = []

for i in temp:
    # temp에서 소문자가 나오면 list에 넣고
    if i.islower():
        listi +=  i
    # 대문자를 소문자로 변환한 것이 listi에 있으면 삭제
    elif i.lower() in listi:
        listi.remove(i.lower())

if listi:
    print('0')
else:
    print('1')