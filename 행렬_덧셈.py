n, m = map(int, input().split())

list1 = []
list2 = []

for _ in range(n): # 왜 packing이 풀려서 들어가는지 모르겠다 # n행 m열
    list1 += [int(i) for i in input().split()]

for _ in range(n): 
    list2 += [int(i) for i in input().split()]

for j in range(n):
    for i in range(m):
        print(list1[i + m*j] + list2[i + m*j], end = ' ')
    print()

