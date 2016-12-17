import math

# LINK FOR PROBLEM: http://codeforces.com/problemset/problem/271/B

## CRIVO

m = 10 ** 5 + 10

eh_primo = [True] * m

eh_primo[0] = False
eh_primo[1] = False

for i in xrange(int(math.sqrt(m))):

    if eh_primo[i]:

        for j in xrange(i * i, m, i):
            eh_primo[j] = False




n, m = map(int, raw_input().split())

rows = []
columns = []
mydict = dict()

# gera matriz
matriz = []
for vez in range(n):
    linha  = map(int, raw_input().split())
    matriz.append(linha)


# conta n_op por linhas
for i in range(n):

    linha = matriz[i]
    n_op = 0
    for j in range(m):

        num = linha[j]
        temp = linha[j]
        count = 0

        if num in mydict:
            n_op = n_op + mydict[num]
        else:
            while not eh_primo[num]:
                num = num + 1
                count = count + 1

            n_op = n_op + count
            mydict[temp] = count

    rows.append(n_op)


# conta n_op por colunas
for i in range(m):

    n_op = 0
    for j in range(n):

        num = matriz[j][i]
        temp = matriz[j][i]
        count = 0

        if num in mydict:
            n_op = n_op + mydict[num]
        else:
            while not eh_primo[num]:
                num = num + 1
                count = count + 1

            n_op = n_op + count
            mydict[temp] = count

    columns.append(n_op)

min_rows = min(rows)
min_columns = min(columns)

if min_rows < min_columns:
    print min_rows
else:
    print min_columns




