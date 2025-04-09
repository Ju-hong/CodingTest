import sys

plate = [[0]*100 for _ in range(100)]#list의 곱은 합처럼(당연함 곱이 합임)

num = int(sys.stdin.readline().strip())

for _ in range(num):
    a, b = map(int, sys.stdin.readline().strip().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            plate[i][j] = 1 

print(sum(sum(row) for row in plate)) # sum of list
'''
black_area = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            black_area += 1

print(black_area) 




total = 0
for k in range(100):
    total += arr[k].count(1)

print(total)

'''
  


'''
sammy = [[0]*2]*4
# matrix의 모든 행이 동일한 row 객체를 참조하게 됩니다. 때문에, 한 행을 수정하면 모든 행이 함께 수정
# matrix[0][0] = 1
# print(matrix[1][0])

sammy2 = [[0]*2 for _ in range(4)]
# 리스트 컴프리헨션을 사용하면, 각 행이 독립적인 리스트가 되도록 만듭니다

print(sammy)
print(sammy2)
'''