# LINK FOR PROBLEM: https://www.urionlinejudge.com.br/judge/pt/problems/view/1451

while True:

    try:
        beiju = ""
        init = ""
        text = str(raw_input())
        home = False

        i = 0
        while i < len(text):
            if text[i] == "[" and not home:
                home = True
            elif text[i] == "[" and home:
                beiju = init + beiju
                init = ""
            elif text[i] == "]":
                beiju = init + beiju
                init = ""
                home = False

            if home:
                if text[i] != "[":
                    init = init + text[i]

            else:
                if text[i] != "]":
                    beiju = beiju + text[i]

            i += 1

        beiju = init + beiju
        print beiju

    except:
        break