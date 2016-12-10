# LINK FOR PROBLEM: http://codeforces.com/problemset/problem/567/A


def mem(positions, i):
    
    maxi = 0
    mini = 0
    
    if positions[i] >= 0: #positivo
    
        maxi = abs( abs(positions[i]) - positions[0] )
        maxii = abs( abs(positions[-1]) - abs(positions[i]) )
        maxi = max(maxi, maxii)

        mini = abs( abs(positions[i]) - positions[i+1] )
        minii = abs( positions[i] - (positions[i-1]))
        mini = min(mini, minii)        
    
    else:
        
        maxi = abs( abs(positions[0]) - abs(positions[i]) )
        maxii = abs( abs(positions[i]) + positions[-1] )            
        maxi = max(maxi, maxii)
            
        mini = abs( abs(positions[i-1]) + positions[i] )
        minii = abs( abs(positions[i]) + positions[i+1] )
        mini = min(mini, minii)
    
        
    return (mini, maxi)

num_city = int( raw_input() )
positions = map(int, raw_input().split())
coast = []

coast.append( ( abs(positions[0]-positions[1]), abs(positions[0]-positions[-1]) ) ) 

for i in xrange(1,  len( positions ) - 1 ):
    coast.append( mem( positions, i) ) 
    
coast.append( ( abs(positions[-1]-positions[-2]), abs(positions[-1]-positions[0]) ) ) 

for tupla in coast:
    print tupla[0],tupla[1]
