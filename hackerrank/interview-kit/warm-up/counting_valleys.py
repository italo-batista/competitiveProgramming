

def countingValleys(n, s):
    level = 0
    n_valleys = 0

    for step in s:
        level = level + 1 if step == 'U' else level - 1
        if level == 0 and step == 'U':
            n_valleys += 1

    return n_valleys
