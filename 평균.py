import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
maxi = max(arr)

temp = [i/maxi*100 for i in arr]

print(sum(temp)/len(temp))
