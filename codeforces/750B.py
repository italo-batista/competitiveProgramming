n = int(raw_input())

North = True
South = False
error = False

dist_from_north = 0

for i in range(n):
    t, dir = map(str, raw_input().split())

    if int(t) > 20000 and (dir == "North" or dir == "South"):
        error = True

    if dist_from_north == 0:
        North = True
        South = False
    elif dist_from_north == 20000:
        South = True
        North = False
    else:
        North = False
        South = False

    if South and dir != "North":
        error = True

    elif North and dir != "South":
        error = True

    if dir == "North":
        dist_from_north = dist_from_north - int(t)

    elif dir == "South":
        dist_from_north = dist_from_north + int(t)

    if dist_from_north < 0 or dist_from_north > 20000:
        error = True


if dist_from_north != 0:
    error = True

if error:
    print "NO"
else:
    print "YES"