#include <iostream>
#include <set>
#include <string>

using namespace std;

set<string> substrings;

int remove_letters(string sequence) {
	
	if (sequence.size() < 1)
		return 0;
	
	int already;	
	string m_sequence;
	substrings.insert(sequence);		
	
	for (int i = 0; i < sequence.size(); i++) {
		
		m_sequence = sequence.substr(0,i) + sequence.substr(i+1);
		already = substrings.count(m_sequence);
		if (already == 0) {
			remove_letters(m_sequence);
		}							
	}	

}

int main() {
	
	string sequence;
    while (cin >> sequence) {

		remove_letters(sequence);
				
		for (set<string>::iterator it = substrings.begin(); 
			it != substrings.end(); it++) {
			cout << *it << endl;
		}
		
		cout << endl;
		substrings.clear();
	}
    return 0;	
}
