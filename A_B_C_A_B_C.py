import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
c = int(sys.stdin.readline().rstrip())

print(sum(map(int, [a, b]))-c, int(a+b)-c, sep ='\n')
