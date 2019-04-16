

def one_away(str1, str2):
    
    i, j, count_op = 0, 0 ,0
    tam1, tam2 = len(str1), len(str2)
    
    while i < tam1 and j < tam2:
    
        if str1[i] != str2[j]:

            if j+1 < tam2 and str1[i] == str2[j+1]:
                # there was an add or delete
                j += 1
                count_op += 1

            elif i+1 < tam1 and str1[i+1] == str2[j]:
                # there was an add or delete
                i += 1
                count_op += 1

            else:
                # so char was raplaced
                count_op += 1
                
        i += 1
        j += 1        
    
    count_op = count_op + tam1 - i
    count_op = count_op + tam2 - j
    
    if count_op > 1:
        return False
    return True


assert one_away('pale', 'ple') == True
assert one_away('pales', 'pale') == True
assert one_away('pale', 'bale') == True
assert one_away('pale', 'bake') == False
assert one_away('palis', 'pale') == False
