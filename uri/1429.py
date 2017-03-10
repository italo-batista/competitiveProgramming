# classic problem of DP: factorial

# BOTTOM UP DP

def factorial(number):

    dp[0] = 1
    dp[1] = 1

    for i in xrange(number+1):
        if dp[i] == float("inf"):
            dp[i] = dp[i - 1] * i



MAX = 100
dp = [float("inf")] * MAX

ant = ""
acm = str(raw_input())

while acm != "0":

    decimal = 0
    tam = len(acm)

    if tam > len(ant): factorial(tam)

    for i in range(tam):
        decimal = decimal + int(acm[i]) * dp[tam-i]

    print decimal

    ant = acm
    acm = str(raw_input())