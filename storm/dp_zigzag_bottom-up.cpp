#include <bits/stdc++.h>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <cstdlib>
#include <algorithm>

#define MAX 51

using namespace std;

int tam, numbers[MAX], dp[MAX][2];

void readInputiInlineWithCommaAndSaveInArray() {
	int n;
	int i = 0;
	string input_with_comma;		
	
	getline(cin, input_with_comma);	
	stringstream ss(input_with_comma);	
	
    while (ss >> n) {        
        numbers[i] = n;
        if (ss.peek() == ',' || ss.peek() == ' ')
            ss.ignore();
        
        i++;
    }
    
    tam = i;
}

int main() {
		    
    readInputiInlineWithCommaAndSaveInArray();
    
    for (int i=0; i<tam; i++)
        dp[i][0] = dp[i][1] = 1;
		
	int res = 1;
			
	for (int i=1; i<tam; i++) {		
		for (int j=0; j<i; j++) {				
			
			if (numbers[j] < numbers[i])
				dp[i][0] = max(dp[i][0], dp[j][1]+1);
			
			if (numbers[j] > numbers[i])
				dp[i][1] = max(dp[i][1], dp[j][0]+1);			
		}
		
		if (res < max(dp[i][0], dp[i][1]))
			res = max(dp[i][0], dp[i][1]);
	}			

	cout << res << "\n";
	return 0;
}


// PROBLEM HERE:
// https://community.topcoder.com/stat?c=problem_statement&pm=1259&rd=4493
