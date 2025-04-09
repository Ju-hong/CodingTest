# 왜 오류?
def cal(a, b):
    count = 0
    while a != b:
        a, b = max(a, b) - min(a, b), min(a, b)
        count += 1
    return count

a, b = map(int, input().split())

print(int(cal(a, b)))


'''
def cal(n, m):
    count = 0
    if n < m:
        n, m = m, n
    elif m == 0:
        return 1

    while m:
        n, m = m, n%m
        count += 1
    return count

n, m = map(int, input().split())

print(int(cal(n, m)))

'''
