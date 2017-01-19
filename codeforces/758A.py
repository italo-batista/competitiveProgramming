
# LINK FOR THE PROBLEM: http://codeforces.com/contest/758/problem/A

n = int(raw_input())
cs = map(int, raw_input().split())
maximo = max(cs)

s = 0
for i in range(n):
    s = s + (maximo - cs[i])

print s
