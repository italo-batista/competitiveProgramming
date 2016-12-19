n = int(raw_input())

comportadas = 0
children = []

for i in range(n):
    ent = map(str, raw_input().split())
    children.append(ent[1])

    if ent[0] == "+":
        comportadas += 1

children.sort()

for child in children:
    print child

print "Se comportaram: %d | Nao se comportaram: %d" % (comportadas, n - comportadas)


