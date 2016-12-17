# LINK FOR PROBLEM: https://www.urionlinejudge.com.br/judge/pt/problems/view/1077

def infixaParaPosfica(inf):

    posf = ""
    pilha = []

    for i in range(len(inf)):

        char = inf[i]

        if char == "(":
            pilha.append(char)

        elif char == ")":
            while True:
                if len(pilha) == 0 or pilha[-1] == "(":
                    break
                else:
                    posf = posf + pilha.pop()

            if len(pilha) > 0:
                pilha.pop()


        elif char == "+" or char == "-":
            while True:
                if len(pilha) == 0 or pilha[-1] == "(":
                    break
                else:
                    posf = posf + pilha.pop()

            pilha.append(char)

        elif char == "*" or char == "/":
            while True:
                if len(pilha) == 0 or pilha[-1] == "(" or pilha[-1] == "+" or pilha[-1] == "-":
                    break
                else:
                    posf = posf + pilha.pop()

            pilha.append(char)

        elif char == "^":
            while True:
                if len(pilha) == 0 or pilha[-1] == "(" or pilha[-1] == "+" or pilha[-1] == "-" or pilha[-1] == "*" or pilha[-1] == "/":
                    break
                else:
                    posf = posf + pilha.pop()

            pilha.append(char)

        else:
            posf = posf + char


    while len(pilha) > 0:
        posf = posf + pilha.pop()

    return posf


n = int(raw_input())

for vez in range(n):

    seq = str(raw_input())
    print infixaParaPosfica(seq)


