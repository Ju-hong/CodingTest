n = int(input()) 
count = 1
bbox = 1

while bbox < n:
    bbox += 6*count
    count += 1

print(count)

# 1 - 1
# [2-8] 6- 2
# [8-20] 12 - 3
# [20-38] 18 - 4
# [38-62] 24 - 5
# 1 + 6*1 + 6*2 + 6*3
