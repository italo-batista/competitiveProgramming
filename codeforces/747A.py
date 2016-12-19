import math

# CRIVO
m = 10 ** 6 + 10
eh_primo = [True] * m
eh_primo[0] = False
eh_primo[1] = False

for i in xrange(int(math.sqrt(m))):

    if eh_primo[i]:
        for j in xrange(i * i, m, i):
            eh_primo[j] = False

# ------------

n = int(raw_input())

a = int(math.sqrt(n))
b = int(math.sqrt(n))

if eh_primo[n]:
    print 1,n

elif a * b == n:
    print a, b

else:

    while a > 0 and a * b < n:
        a = a - 1

    if a * b != n:

        a = int(math.sqrt(n))
        while a * b < n:
            if a * (b+1) > n:
                a = a - 1
            else:
                b = b + 1

    print a, b
