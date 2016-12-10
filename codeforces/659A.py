# LINK FOR PROBLEM: http://codeforces.com/problemset/problem/659/A


ent = map(int, raw_input().split())

n = ent[0]
a = ent[1]
b = ent[2]

print ( (a - 1 + b) % n + n) % n + 1
