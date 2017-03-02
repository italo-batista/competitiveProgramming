# helped a lot: http://mattleao.blogspot.com.br/2015/03/percurso-em-arvore-e-problemas-1194-uri.html

c = int(raw_input())

while c > 0:

    posf = []
    current = [-1]

    def posfixa(preordem, inordem, bottom, top):

        if (bottom <= top):

            # pega o index da raiz da atual subarvore
            cur = current[0] + 1
            current[0] = cur
            # encontra o index dessa raiz no inordem para poder fazer o "partition"
            index = inordem.index(preordem[cur])

            # parece o partition do quicksort
            posfixa(preordem, inordem, bottom, index - 1)
            posfixa(preordem, inordem, index + 1, top)
            posf.append(inordem[index])

    entrada = map(str, raw_input().split())
    n = int(entrada[0])
    pref = entrada[1]
    inf = entrada[2]

    posfixa(pref, inf, 0, n-1)

    print "".join(posf)

    c = c - 1
