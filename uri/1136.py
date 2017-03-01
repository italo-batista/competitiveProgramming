n, b = map(int, raw_input().split())

while n != 0 and b != 0:

    bi = map(int, raw_input().split())

    flag = False
    mapa = {}
    for i in range(n+1):
        mapa[i] = False

    for x in bi:
        for y in bi:
            num = abs(x - y)
            mapa[num] = True

    for i in range(n+1):
        if mapa[i] == False:
            flag = True
            break

    if flag:
        print "N"
    else: print "Y"

    n, b = map(int, raw_input().split())