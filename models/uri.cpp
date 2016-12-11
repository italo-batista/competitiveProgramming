#include <bits/stdc++.h>
#include <iostream>
#include <cstdlib>
#define ll long long int
using namespace std;



ll power (ll number, ll p);

int main() {
	int n;
	ll s;
	
	scanf("%d",&n);
	s = n;
	s = power(3, s);
	
	printf("%llu\n", s);
	return 0;
}

ll power (ll number, ll p) {
	if (p == 0)	return 1;
	if (p % 2 == 0) return power((number*number) % 2147483647, p/2) % 2147483647;
	else return number * power(number%2147483647, p-1) % 2147483647;
}


