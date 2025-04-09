def gcd(a, b):
    if a <  b:
        a, b = b, a

    while b:
        a, b = b, a%b
    return a


n, m = map(int, input(). split())

print(gcd(n, m), n*m//gcd(n, m), sep='\n')

