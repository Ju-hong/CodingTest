goal = [_ for _ in range(1, 9)]
temp = list(map(int, input().split()))

if temp == goal:
    print("ascending")
elif temp == goal[::-1]:
    print("descending")
else:
    print("mixed")


'''
a = "1 2 3" # string 각 문자(공백 포함)이 list의 원소가 됨
print(list(a))
'''