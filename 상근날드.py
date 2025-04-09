import sys

mina = min([int(sys.stdin.readline()) for _ in range(3)])
# sys.stdin.readline().strip().int()는 strip() 메서드가 반환한 문자열 객체에 대해 int() 메서드를 호출하려고 합니다. 하지만 문자열 객체에는 int() 메서드가 없기 때문에 에러가 발생합니다.
# 문자열 객체는 다양한 메서드를 가지고 있지만, int()는 그 중 하나가 아닙니다.
minb = min([int(sys.stdin.readline()) for _ in range(2)])

print(mina+minb-50)
