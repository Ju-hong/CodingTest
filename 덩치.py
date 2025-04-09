import sys

n = int(sys.stdin.readline().rstrip())

temp = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
enum_temp = [_ for _ in enumerate(temp)]
print(max(enum_temp[i][1][1] for i in range(n)))