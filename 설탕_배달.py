def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


n = int(input())

print(fibo(n))

# 1 1 2 3 5 8
# 0 1 2 3 4 5