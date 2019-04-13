

def sockMerchant(n, ar):
    count_socks = dict()
    for sock_color in ar:
        count_socks[sock_color] = count_socks.get(sock_color, 0) + 1
    pairs = 0
    for k, v in count_socks.items():
        pairs += (v/2)
    return pairs
