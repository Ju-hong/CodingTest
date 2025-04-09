import sys

arr = list(map(int, sys.stdin.readlines()))

fibo_list = [0, 1, 1]

for i in range(2, max(arr)):
    fibo_list.append(fibo_list[i-1] + fibo_list[i-2])

print(fibo_list)
'''
for i in arr:
    num = int(input())
    if num == -1:
        break

    else:
        effect = 1
        print(f'Hours {num}: {effect} cow(s) affected')
'''

