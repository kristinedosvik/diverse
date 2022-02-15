/*
#### Count operations manual from c code ####
input:
Matrix 1: C1, R1.
Matrix 2: C2, R2.

main:
set matrix1
set matrix2
if
mulMat:
	define matrix
	print
	for R1:
		for C2:
			set
			for R2:
				set
			print
		print

num operasjoner:
C1*R1 + C2*R2 + 1 + 1 + 1+ R1*(C2*(1+R2*(1)+1)+1)
*/

/*
Complexity:

 */

#include <stdio.h>

int main(){
	int C1 = 4;
	int R1 = 4;
	int C2 = 4;
	int R2 = 4;
	
	int manual_c = C1*R1 + C2*R2 + 1 + 1 + 1+ R1*(C2*(1+R2*(1)+1)+1);
	int complexity = C1*C2*R2;

	printf("Manual count c code: %d\n", manual_c);
	printf("Complexity: %d\n", complexity);
	
	return 0;
}

