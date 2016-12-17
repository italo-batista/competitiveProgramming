# LINK FOR PROBLEM: https://www.urionlinejudge.com.br/judge/pt/problems/view/2064

def trocaCntaFavotiras(nome, l1, l2):
    count = 0
    tam = len(nome)
    for i in range(tam):

        if nome[i] == l1:
            if i == len(nome):
                nome = nome[:i] + l2
            else:
                nome = nome[:i] + l2 + nome[i + 1:]
        elif nome[i] == l2:
            if i == len(nome):
                nome = nome[:i] + l1
            else:
                nome = nome[:i] + l1 + nome[i + 1:]

        if nome[i] in favoritas:
            count = count + 1

    nomes[nome] = count
    return nome


k, m, n = map(int, raw_input().split())
favoritas = str(raw_input())
nome = str(raw_input())
nomes = dict()


count = 0
for i in range(len(nome)):
    if nome[i] in favoritas:
        count = count + 1
nomes[nome] = count


for i in range(n):
    troca = map(str, raw_input().split())
    nome = trocaCntaFavotiras(nome, troca[0], troca[1])

valor = max(nomes.values())
index = nomes.values().index(valor)
melhor_nome = nomes.keys()[index]

print valor
print melhor_nome

