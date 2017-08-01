# ALGORTIMO GULOSO

# http://olimpiada.ic.unicamp.br/pratique/programacao/nivelj/2010f2pj_dentista

TERMINO_DE_CONSULTA = 1
INICIO_DE_CONSULTA = 0

n = input()

consultas = []
for i in xrange(n):
	x, y = map(int, raw_input().split())
	consultas.append((x, y))
	
consultas = sorted(consultas, key=lambda x: x[TERMINO_DE_CONSULTA])	

contador = 0
fim_ultima_consulta = 0

for consulta in consultas:
		if consulta[INICIO_DE_CONSULTA] >= fim_ultima_consulta:
			fim_ultima_consulta = consulta[TERMINO_DE_CONSULTA]
			contador += 1

print contador


# tutorial: http://noic.com.br/informatica/curso-noic-de-informatica/aula-12-algoritmo-guloso/
