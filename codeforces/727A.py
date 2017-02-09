# LINK FOR PROBLEM: http://codeforces.com/problemset/problem/727/A

def ends_with_one(number):
    number = str(number)
    return number[-1] == "1"

def del_last_one(number):
    number = str(number)
    t = len(number)
    number = int( number[:t-1] )
    return number

def isEven(number):
    return (number % 2 == 0)


a, b = map(int, raw_input().split())
fila = [str(b)]

current_number = b

while current_number > a:

    if ends_with_one(current_number):
        current_number = del_last_one(current_number)
        fila.append(str(current_number))

    elif isEven(current_number):
        current_number = current_number / 2
        fila.append(str(current_number))

    else:
        current_number = a-1
        break

if current_number < a:
    print "NO"

elif current_number == a:

    print "YES"
    print len(fila)
    print " ".join(str(fila[i]) for i in range(len(fila)-1, -1, -1 ))






