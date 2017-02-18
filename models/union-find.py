# n : numero de nos
# q : numero de operacoes


n, q = map(int, raw_input().split())

parents = range(n+1)
sizes = [1] * (n+1)

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
		parent_x = get_parent(x)
		parent_y = get_parent(y)

        if sizes[parent_x] > sizes[parent_y]:
            parents[parent_y] = parent_x
            sizes[parent_x] += sizes[parent_y]

        else:
            parents[parent_x] = parent_y
            sizes[parent_y] += sizes[parent_x]

def get_size(x):
	return sizes[get_parent(x)]

