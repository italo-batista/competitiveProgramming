#include<stdio.h>


int main() {

	long int testes;
	scanf ("%ld", &testes);
	
	for(int i = 0; i < testes; i++) {
		
		long int n, cidade_um, comida_um, total;
		scanf ("%ld", &n);
		
		long int cidades[n];
		long int comidas[n];
		
		scanf ("%ld %ld", &cidade_um, &comida_um);		
		cidades[0] = cidade_um;
		comidas[0] = comida_um;
		
		
		total = 0;
		for(int j = 1; j < n; j++) {
			
			long int cidade, comida;
			scanf ("%ld %ld", &cidade, &comida);
			
			cidades[j] = cidade;
			comidas[j] = comida;			
			
			if ( (cidades[j] - cidades[j-1]) * cidades[j-1] > comidas[j-1] ) {
				total = total + (cidades[j] - cidades[j-1]) * cidades[j-1] - comidas[j-1];
			}
			
		}
		
		total = total - comidas[n-1];
		
		if (total <= 0) {
			printf ("Perde %ld", -total);
		} else {
			printf ("Ganha %ld", total);
		}
		
	
	}
	

 
	return 0;
}
