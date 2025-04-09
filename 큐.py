import sys

n = int(sys.stdin.readline().strip())

temp = []

for _ in range(n):
    n = sys.stdin.readline().strip().split()
    if n[0] == 'push':
        temp.append(int(n[1]))
        
    elif n[0] == 'pop':
        if temp:
            print(temp.pop(0))
        else:
            print(-1)

    elif n[0] == 'size':
        print(len(temp))

    elif n[0] == 'empty':
        if temp:
            print(0)
        else:
            print(1)

    elif n[0] == 'front':
        if temp:
            print(temp[0])
        else:
            print(-1)

    elif n[0] == 'back':
        if temp:
            try:
                print(temp[-1])
            except:
                print(temp[0])

        else:
            print(-1)

    