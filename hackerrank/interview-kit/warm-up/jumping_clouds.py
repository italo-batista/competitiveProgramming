

def jumpingOnClouds(c, n):
    i = 0
    jumps = 0
    while i < (n-1):
        if i+2 < n and c[i+2] == 0:
            i += 2
        else:
            i += 1
        jumps += 1
    return jumps


if __name__ == '__main__':

    n = int(raw_input())

    c = map(int, raw_input().rstrip().split())

    print jumpingOnClouds(c, n)

