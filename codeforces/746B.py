tam = int(raw_input())
encode = str(raw_input())

word = [""] * tam
letters = tam

if tam % 2 == 0:
    mid = tam / 2 -1
else:
    mid = tam / 2

i = mid
curr = 0
if tam % 2 != 0:
    while letters > 0:

        if curr < tam:

            if curr == 0:
                word[mid] = encode[curr]
                curr = curr + 1

            elif curr % 2 != 0:
                i = mid - (i - mid) - 1
                word[i] = encode[curr]
                curr = curr + 1

            else:
                i = mid + (mid - i)
                word[i] = encode[curr]
                curr = curr + 1

            letters = letters - 1

        else:
            break
else:
    while letters > 0:

        if curr < tam:

            if curr == 0:
                word[mid] = encode[curr]
                curr = curr + 1

            elif curr % 2 != 0:
                i = mid + (mid - i) + 1
                word[i] = encode[curr]
                curr = curr + 1

            else:
                i = mid - (i - mid)
                word[i] = encode[curr]
                curr = curr + 1

            letters = letters - 1

        else:
            break


print "".join(word)