x = int(raw_input())

pessoa = dict()

for i in range(x):
    ent = map(str, raw_input().split())

    gifts = []
    gifts.append(ent[1])
    gifts.append(ent[2])
    gifts.append(ent[3])

    pessoa[ent[0]] = gifts

while True:

    try:
        ent = map(str, raw_input().split())

        nome = ent[0]
        opcao = ent[1]


        if nome in pessoa and opcao in pessoa[nome]:
            print "Uhul! Seu amigo secreto vai adorar o/"
        else:
            print "Tente Novamente!"


    except:
        break