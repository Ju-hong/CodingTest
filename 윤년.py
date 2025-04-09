a = int(input())

print(1) if (not a%400) or ((not a%4) and (a % 100)) else print(0)
    