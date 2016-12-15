# LINK FOR PROBLEM: https://www.urionlinejudge.com.br/judge/en/problems/view/2345

ent =  map(int, raw_input().split())

first = 0
second = 0

first = max(ent)
ent.remove(first)

second = max(ent)
ent.remove(second)

if first > second:
	second += max(ent)
	first += min(ent)
else:
	second += min(ent)
	first += max(ent)
	
if first > second:
	print first - second
else:
	print second - first
	




