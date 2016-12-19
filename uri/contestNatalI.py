
congrats = dict()
n = int(raw_input())

for i in range(n):
    idiom = str(raw_input())
    trad = str(raw_input())
    congrats[idiom] = trad

m = int(raw_input())
for i in range(m):
    name = str(raw_input())
    idiom = str(raw_input())

    msg = name + "\n" + congrats[idiom] + "\n"
    print msg
