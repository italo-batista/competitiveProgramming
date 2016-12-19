
p, a = map(int, raw_input().split())

valor_last = 0
total = 0
salario = 0
c = 0
for presente in range(p):

    valor = int(raw_input())

    if presente != 0 and valor * 2 >= valor_last:
        total = total + salario * c
        c = 0
        salario = 0
        valor_last = valor
        print 'aqui'
    else:
        print 'acola'
        c = c + 1
        salario = salario + valor

    print valor, salario, c, total

print total
