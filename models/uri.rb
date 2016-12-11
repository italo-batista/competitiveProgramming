valor = gets.to_f
temp = valor

n100 = (temp - (temp % 100)) / 100
temp = temp % 100

n50  = (temp - (temp % 50))  / 50
temp = temp % 50

n20  = (temp - (temp % 20))  / 20
temp = temp % 20

n10  = (temp - (temp % 10))  / 10
temp = temp % 10

n5   = (temp - (temp % 5))   / 5
temp = temp % 5

n2   = (temp - (temp % 2))   / 2
temp = temp % 2


puts "NOTAS:"
puts "%d nota(s) de R$ 100.00" % n100
puts "%d nota(s) de R$ 50.00" % n50
puts "%d nota(s) de R$ 20.00" % n20
puts "%d nota(s) de R$ 10.00" % n10
puts "%d nota(s) de R$ 5.00" % n5
puts "%d nota(s) de R$ 2.00" % n2


m1   = (temp - (temp % 1))    / 1
temp = temp % 1

m50  = (temp - (temp % 0.5))  / 0.5
temp = temp % 0.5

m25  = (temp - (temp % 0.25)) / 0.25
temp = temp % 0.25

m10  = (temp - (temp % 0.1))  / 0.1
temp = temp % 0.1

m5   = (temp - (temp % 0.05)) / 0.05
temp = temp % 0.05

temp = (100*n100 + 50*n50 + 20*n20 + 10*n10 + 5*n5 + 2*n2 + 1*m1 + 0.5*m50 + 0.25*m25 + 0.1*m10 + 0.05*m5)
print temp
m01 = valor - temp

#m01   = (temp - (temp % 0.01)) / 0.01
#temp = temp % 0.01

puts "MOEDAS:"
puts "%d moeda(s) de R$ 1.00" % m1
puts "%d moeda(s) de R$ 0.50" % m50
puts "%d moeda(s) de R$ 0.25" % m25
puts "%d moeda(s) de R$ 0.10" % m10
puts "%d moeda(s) de R$ 0.05" % m5
puts "%d moeda(s) de R$ 0.01" % m01


