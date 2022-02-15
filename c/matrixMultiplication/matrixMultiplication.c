#include <stdio.h>
#include <time.h>
#include <stdlib.h>
  
// Edit MACROs here, according to your Matrix Dimensions for mat1[R1][C1] and mat2[R2][C2]
#define R1 100            // number of rows in Matrix-1
#define C1 100           // number of columns in Matrix-1
 
void mulMat(int mat1[][C1], int mat2[][C1]) {
    int rslt[R1][C1];
  
    for (int i = 2; i < R1; i++) {
        for (int j = 2; j < C1; j++) {
            rslt[i][j] = 0;
 
            for (int k = 2; k < R1; k++) {
                rslt[i][j] += mat1[i][k] * mat2[k][j];
            }
        }
    }
}
int main(int argc, char* argv[]) {
    
    if(argc == 2){
	printf("time stamp file: %s\n", argv[1]);
    }else{
	printf("Error: wrong input sequence\n");
	return -1;
    }
	
    clock_t start, end;
    int mat1[R1][C1], mat2[R1][C1];
    FILE *fptr;

    for (int i = 0; i < R1; i++){
	for (int j = 0; j < C1; j++){
		mat1[i][j] = rand();
		mat2[i][j] = rand();
	}
    }
	
     if (C1 != R1) {
     printf("The number of columns in Matrix-1  must be equal to the number of rows in "
                "Matrix-2");
        printf("Please update MACROs according to your array dimension in #define section");
        return -1;
    }

    fptr = fopen(argv[1], "a");
    for (int i = 0; i < 100; i++){
	    start = clock();
	    mulMat(mat1, mat2);
	    end = clock();
	    float time_used = ((float)(end - start)) / CLOCKS_PER_SEC;
	   
	    fprintf(fptr, "%i %f\n", R1*C1, time_used);
    }
    fclose(fptr);
    return 0;

}

