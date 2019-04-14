
def repeatedString(s, n):
    count_a = 0
    resto = n % len(s)
    repeated = n / len(s)

    for i in range(len(s)):
        if s[i] == 'a':
            if i < resto:
                count_a += 1
            count_a += repeated

    return count_a


