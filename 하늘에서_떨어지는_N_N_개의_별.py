#0
import math

n, d, k = map(int, input().split())
arr = list(map(int, input().split()))

doom_cycle = k//max(arr)

print(math.ceil((d-doom_cycle)/doom_cycle))
# 첫 번째 주기(doom_cycle일)는 청소 없이 지낼 수 있습니다.
# 남은 날짜(d-doom_cycle)를 각 주기(doom_cycle)로 나누고 
# 올림하여 필요한 청소 횟수를 계산합니다.

# 처음 2일은 청소 없이 지낼 수 있습니다.(0일차부터 시작해서 1일차 밤까지)
# 남은 3일(d-doom_cycle = 5-2 = 3)을 관리해야 합니다.
# 2일마다 청소해야 하므로, 3/2 = 1.5회의 청소가 필요합니다.

#만약 내림을 하면 1회만 청소하게 되는데, 이는 2일만 더 관리할 수 있다는 의미입니다.
#하지만 남은 일수는 3일이므로, 1회 청소로는 폭발을 막을 수 없습니다.
#따라서 올림하여 2회 청소해야 3일 동안 폭발 없이 관리할 수 있습니다.

# (d-doom_cycle)/doom_cycle의 값이 정수가 아닐 때, 우리는 반드시 추가 청소를 해야 합니다. 

# n.5일을 관리하기 위해서는 n+1회의 청소가 필요합니다.

# 전체 d에서 관리 없이 지낼 수 있는 doom_cycle을 빼주고,
# 남은 값은 온전히 관리되어야 하기 때문에 ceil로 올려준다.


#1
n, d, k = map(int, input().split())
s=list(map(int,input().split()))

print((d-1)//(k//max(s)))
# 하지만 D-1을 사용하는 이유는, D일째에는 청소가 필요 없기 때문입니다. 
# D일 끝에 폭발해도 우리의 관리 기간은 끝나므로
