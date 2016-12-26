# LINK FOR PROBLEM: http://codeforces.com/problemset/problem/625/C

n, k = map(int, raw_input().split())

m = [] * n
v = n * n
sum = 0

for i in range(n):

    row = [0] * n
    for j in range(n-1, k-2, -1):
        row[j] = str(v)
        v = v -1

    sum = sum + v + 1
    m.append(row)

for i in range(n):

    for j in range(k-2, -1, -1):

        m[i][j] = str(v)
        v = v - 1

ans = ""
for i in range(n):
    row = " ".join(m[i])
    ans = ans + row + "\n"



print sum
print ans


