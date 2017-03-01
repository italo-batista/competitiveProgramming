

while True:

    try:
        x, y = map(int, raw_input().split())
        bin_x = int("{0:b}".format(x))
        bin_y = int("{0:b}".format(y))

        temp = str(bin_x + bin_y)

        tam = len(temp)
        result = 0
        for i in range(tam):

            if temp[i] == "1":
                result = result + 2 ** (tam - 1 - i )

        print result

    except:
        break

