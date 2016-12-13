#include<stdio.h>

/* LINK FOR PROBLEM: http://www.spoj.com/problems/BSEARCH1/ */

int findLowerIndex(long int currentI, long int x, long int i, long int v[]) {
	long int tempI;
	tempI = currentI;
	
	while (tempI > i && v[tempI] == v[tempI-1]) {	
		tempI--;
	}
	
	return tempI;
} 

int buscaBinaria(long int x, long int i, long int j, long int v[]) {

   long int mid;
   
   if ((i > j) || (v[i] > x) || (v[j] < x)) {
   	return -1;
   }
   
   else {
   	
   	mid = (i + j) / 2;

   	if (x == v[mid]) {
   		return findLowerIndex(mid, x, i, v);
   	}
   	
   	else if (v[mid] < x) {
   		return buscaBinaria(x, mid+1, j, v);
   	}
   	
   	else {
   		return buscaBinaria(x, i, mid-1, v);
   	}
   	
   }                          
}  



int main() {

	long int n, q, k;
	long int array[100000];
	scanf ("%ld %ld", &n, &q);
	for (int l = 0; l < n; l++)
		scanf ("%ld", &array[l]);
	for (int l = 0; l < q; l++) {
		scanf ("%ld", &k);
		printf ("%d\n", buscaBinaria(k, 0, n-1, array));
	}
 
	return 0;
}
