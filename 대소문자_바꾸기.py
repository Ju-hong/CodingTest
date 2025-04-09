import sys

m = sys.stdin.readline().strip()
temp = []

for i in m:
    if i.islower():
        temp.append(i.upper())
    elif i.isupper():
        temp.append(i.lower())

print(''.join(temp))