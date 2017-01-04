

n, k = map(int, raw_input().split())
time = (60 * 4) - k

qst = 0

for i in range(1,n+1,1):

    if (time - 5*i) >= 0:
        qst += 1
        time -= (5*i)
    else:
        break


print qst

