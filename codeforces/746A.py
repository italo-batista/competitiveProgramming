a = int(raw_input())
b = int(raw_input())
c = int(raw_input())

n_a = a
n_b = 0
n_c = 0

if c != 0 and c >= 4:
    n_c = c / 4

if b != 0 and b >= 2:
    n_b = b / 2


m = min([n_c, n_a, n_b])

n_a = m * 1
n_b = m * 2
n_c = m * 4

print sum([n_a, n_b, n_c])



