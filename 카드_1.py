temp = [i for i in range(1, int(input())+1)]
goal = []

for _ in range(len(temp)):
    try: 
        goal.append(temp.pop(0))
        temp.append(temp.pop(0))
    except:
        goal += temp


print(*goal, sep =" ")
