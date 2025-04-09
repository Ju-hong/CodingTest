import sys


temp = []

for i in range(int(input())):
    put = sys.stdin.readline().strip().split()
    
    if put[0] == 'push':
        temp.append(int(put[1]))


    elif put[0] == 'pop':
        try: 
            print(temp.pop())
        except:
            print(-1)


    elif put[0] == 'size':
        print(len(temp))


    elif put[0] == 'empty':
        if temp:
            print(0)
        else:
            print(1)


    elif put[0] == 'top':
        try:
            print(temp[-1])
        except:
            print(-1)
