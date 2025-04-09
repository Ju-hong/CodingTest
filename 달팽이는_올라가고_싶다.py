import math

a, b, v = map(int, input().split())

print(math.ceil((v-a)/(a-b)+1))

# d(a-b) + b*1 >= v
# 미끄러지면서 v-a 도착까지 필요한 밤낮 일수를 구한다
# v-a 위치에서 올리면 그대로 정수
# v-a+1, ..., v-1 위치라면 완전히 나누어떨어지지 않으므로(소수)
# 날짜는 올려준다
'''

a,b,v=map(int,input().split())
print(1-(v-a)//(b-a))

'''
'''
# 그러나 식을 (V-A)/(A-B)로 쓰면, 달팽이가 첫 날에 A만큼 올라가서 바로 정상에 도달하는 경우(V≤A)를 처리하기 어렵습니다.
# k = (v-b)/(a-b)에서 (v-b)/(a-b)회만큼 달팽이는 이동한다
# +a-b +a-b +a == v
# +a-b +a-b +a-b = v-b
# a는 항상 b보다 크므로
# (v-b)/(a-b)이 정수인 경우, 마지막 날 달팽이의 이동은 분모에 b만큼의 미끄러짐 없이 +a로 끝난다
# 즉, 마지막 날 정상에서 미끄러져 v-b 위치에 도달할 때, 달팽이의 밤낮 이동거리는 a-b는 일관되게 a-b이다.
# 순 이동거리를 기준으로 마지막날 위치해야할 거리가 v-b인 것이다.


# a*k-b*(k-1) => v
## k>=(v-b)/(a-b)

a,b,v = map(int,input)
k = (v-b)/(a-b)
print(int(k) if k == int(k) else int(k)+1)
'''
