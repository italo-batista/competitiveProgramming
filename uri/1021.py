import math

# LINK FOR PROBLEM: https://www.urionlinejudge.com.br/judge/pt/problems/view/1021
	
valor = float(raw_input())
temp = valor

notas = [100.0, 50.0, 20.0, 10.0, 5.0, 2.0]
moedas = [1.00, 0.50, 0.25, 0.10, 0.05]

print "NOTAS:"
for nota in notas:
	ni = (temp - (temp % nota)) / nota
	temp = temp % nota
	print "%d nota(s) de R$ %1.2f" % (ni, nota)

print "MOEDAS:"
for moeda in moedas:
	mi  = (temp - (temp % moeda)) / moeda
	temp = temp % moeda
	print "%d moeda(s) de R$ %1.2f" % (mi, moeda)


# caso especial = moeda de 0.01
temp = float("%1.2f" % temp) * 100
mi  = (temp - (temp % 1)) / 1
print "%d moeda(s) de R$ %1.2f" % (mi, 0.01)
