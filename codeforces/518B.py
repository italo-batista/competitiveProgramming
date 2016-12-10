# LINK FOR PROBLEM: http://codeforces.com/problemset/problem/518/B

ans1 = 0
ans2 = 0

s = str(raw_input())
t = str(raw_input())

count = {}

for letter in t:
    if letter in count:
        count[letter] += 1
    else:
        count[letter] = 1    
        
for i in range(len(s)):
	
	l = s[i].lower()
	L = t[i].lower()
	
	if count.has_key(s[i]) and count[ s[i] ] > 0:
		ans1 += 1
		count[ s[i] ] -= 1
	
	elif l == L:
		
		if count.has_key(s[i].upper()) and s[i] != s[i].upper():
			if count[s[i].upper()] > 0:
				ans2 += 1
				count[s[i].upper()] -= 1
		elif count.has_key(s[i].lower()) and s[i] != s[i].lower():
			if count[s[i].lower()] > 0:
				ans2 += 1
				count[s[i].lower()] -= 1
    
print ans1,ans2
