import sys





N = int(sys.stdin.readline())
cards = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))


print(" ".join("1"  if i in cards else "0" for i in targets))






