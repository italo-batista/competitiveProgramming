# LINK FOR PROBLEM: https://www.urionlinejudge.com.br/judge/pt/problems/view/2064

def trocaLetras(name, l1, l2):
    count = 0
    temp = dict()

    for letter in name:

        if letter == l1:
            value = name[letter]
            temp[l2] = value
            if l2 in favoritas:
                count = count + temp[l2]

        elif letter == l2:
            value = name[letter]
            temp[l1] = value
            if l1 in favoritas:
                count = count + temp[l1]

        else:
            temp[letter] = name[letter]
            if letter in favoritas:
                count = count + name[letter]

    return (temp, count)


k, m, n = map(int, raw_input().split())
favoritas = str(raw_input())
bestname = str(raw_input())
nomes = dict()
nome = dict()
VEZ = 0
trocas = []

count = 0
for i in range(len(bestname)):
    letra = bestname[i]

    if letra in favoritas:
        count = count + 1

    if letra in nome:
        nome[letra] = nome[letra] + 1
    else:
        nome[letra] = 1

nomes[VEZ] = count
VEZ += 1

for i in range(n):
    troca = map(str, raw_input().split())
    trocas.append((troca[0], troca[1]))

    tupla = trocaLetras(nome, troca[0], troca[1])
    nome = tupla[0]
    nomes[VEZ] = tupla[1]

    VEZ += 1

valor = max(nomes.values())
index = nomes.values().index(valor)
melhor_vez = nomes.keys()[index]

for j in range(melhor_vez):

    letras = trocas[j]
    l1 = letras[0]
    l2 = letras[1]

    for i in range(len(bestname)):

        if bestname[i] == l1:
            if i == len(bestname):
                bestname = bestname[:i] + l2
            else:
                bestname = bestname[:i] + l2 + bestname[i + 1:]
        elif bestname[i] == l2:
            if i == len(bestname):
                bestname = bestname[:i] + l1
            else:
                bestname = bestname[:i] + l1 + bestname[i + 1:]


print valor
print bestname

