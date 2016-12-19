def conta_ocorrencias(s, w):

    c = 0
    j = 0
    while j <= (len(w) - len(s)):

        if w[j] == s[0]:

            flag = True
            for l in range(len(s)):
                if w[l+j] != s[l]:
                    flag = False

            if flag:
                c = c + 1
                j = j + len(s) - 1

        j = j + 1
    return c

word = str(raw_input())
tam = len(word)
maior = (0,0)

if len(word.split(word[0])) - 1 == len(word):
    print 1
elif len(word) % 2 != 0:
    print len(word)
else:

    for i in range(2, tam + 1, 1):
        seq = word[:i]
        ocorrencias = conta_ocorrencias(seq, word)

        if ocorrencias >= maior[1]:
            maior = (i, ocorrencias)

    print maior[0]
