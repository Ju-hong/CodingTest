import sys

dicti = {'A+': 4.5,'A0': 4.0,'B+': 3.5,'B0': 3.0,'C+': 2.5,'C0': 2.0,'D+': 1.5,'D0': 1.0,'F': 0}
temp = []

for _ in range(20):
    _, n, m = sys.stdin.readline().strip().split()
    
    if m != 'P':
        temp.append([float(n), dicti[m]])

sumi = 0
muli = 0

for i in temp:
    sumi += i[0]*i[1]
    muli += i[0]

print(f"{sumi/muli:.6f}")
