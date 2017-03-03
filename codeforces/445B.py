def get_parent(x):
	if x == parents[x]:
		return parents[x]
	else:
		parents[x] = get_parent(parents[x])
		return parents[x]

def same_set(x, y):
	return get_parent(x) == get_parent(y)

def connect(x, y):

    if not same_set(x, y):

        if sizes[get_parent(x)] > sizes[get_parent(y)]:
            parents[get_parent(y)] = get_parent(x)
            sizes[get_parent(x)] += sizes[get_parent(y)]

        else:
            parents[get_parent(x)] = get_parent(y)
            sizes[get_parent(y)] += sizes[get_parent(x)]

def get_size(x):
	return sizes[get_parent(x)]

n, m = map(int, raw_input().split())

danger = 1
parents = range(n+1)
sizes = [1] * (n+1)

for i in range(m):

    a, b = map(int, raw_input().split())

    if not same_set(a, b):
        danger = danger * 2

    connect(a, b)

print danger