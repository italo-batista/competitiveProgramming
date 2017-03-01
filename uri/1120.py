zero = "0"
n, b = map(str, raw_input().split())

while n != zero and b != zero:

    temp = "".join([x for x in b if x != n])
    if temp == "":
        print 0
    else:
        print int(temp)

    n, b = map(str, raw_input().split())