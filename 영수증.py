import sys

final = int(sys.stdin.readline().strip())

sumi = sum([int(sys.stdin.readline().strip()) for _ in range(9)])

print(final - sumi)