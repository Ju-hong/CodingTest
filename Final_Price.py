import sys

_, *args = map(int, sys.stdin.readlines()) #n과 args라는 이름의 원소
print(sum(args))