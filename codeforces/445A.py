
n, m = map(int, raw_input().split())

for i in range(n):

    linha = str(raw_input())
    saida = ""
    for j in range(m):

        if i % 2 == 0:

            if linha[j] == ".":
                if j % 2 == 0:
                    saida += "B"
                else:
                    saida += "W"

            else:
                saida += "-"

        else:

            if linha[j] == ".":
                if j % 2 == 0:
                    saida += "W"
                else:
                    saida += "B"

            else:
                saida += "-"

    print saida