
while True:

    try:
        n, k = map(int, raw_input().split())
        people = map(int, raw_input().split())

        dists = [0]
        fila = [0]
        fila.extend(people)

        for i in range(1, n, 1):
            dist = fila[i] - fila[i-1]
            dists.append(dist)

        dists.sort(reverse=True)
        print sum(dists[k-1:n])

    except: break


