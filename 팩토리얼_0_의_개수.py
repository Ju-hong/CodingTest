
n = int(input())
a = 1
count = 0

for i in range(1, n+1):
    a *= i

a = str(a)[::-1]

for j in a:
    if j == '0':
        count +=1
    else:
        break

print(count)

###
N = int(input())

print(N//5 + N//25 + N//125)


