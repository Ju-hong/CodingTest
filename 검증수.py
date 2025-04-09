import sys



temp = list(map(int, sys.stdin.readline().strip().split()))
print(sum([i**2 for i in temp])%10)
