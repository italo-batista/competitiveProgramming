testes = int(raw_input())

for teste in range(testes):

    n =  int(raw_input())

    cidades = [0] * n
    comidas = [0] * n

    ent = map(int, raw_input().split())
    cidades[0] = ent[0]
    comidas[0] = ent[1]

    total = 0
    for i in range(1, n):

        ent = map(int, raw_input().split())
        cidades[i] = ent[0]
        comidas[i] = ent[1]

        if (cidades[i] - cidades[i-1]) * cidades[i-1] > comidas[i-1]:
            total = total + (cidades[i] - cidades[i-1]) * cidades[i-1] - comidas[i-1]

    total = total - comidas[n-1]

    if total <= 0:
        print "Perde %d" % abs(total)
    else:
        print "Ganha %d" % abs(total)