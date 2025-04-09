import sys

a, b, c = map(int, sys.stdin.readlines())
dict_i = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}

for i in str(a*b*c):
    dict_i[i] += 1

for j in range(len(dict_i)):
    print(dict_i[str(j)])

# for i in range(10): list(map(int,str(res))).count(i)
# listi = [0]*10; for i in str(a*b*c): listi[int(i)] += 1; for j in listi: print(j)