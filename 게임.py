






'''
count, win = map(int, input().split())
last = 1-(win/count-win//count)


for i in range(count):
    if count == win:
        print(-1)
        break
    elif (win+i)/(count+i) >= (last + win/count):
        print(i)
        break
    else:
        continue
        
'''