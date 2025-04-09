h, m = map(int, input().split())
t = int(input())

if m + t > 59:
    h += (m+t)//60
    
m = (m+t)%60

if h >= 24:
    h = h-24


print(h, m)