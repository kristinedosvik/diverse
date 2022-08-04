#include <stdio.h>
#include <stdlib.h>


/*
typedef struct Ingrediens {
   //char ** nearingsstoffer;
   //char nearingsstoffer[5][5];
   //char number[2][6];
   char * number;
} Ingrediens;


typedef struct Matoversikt {
   Ingrediens fisk[2];
   Ingrediens * kjott;
   Ingrediens * meieri_and_egg;
   Ingrediens * plantebasert;
} Matoversikt;

#define NUMBER_OF_ELEMENTS_1 5
#define NUMBER_OF_ELEMENTS_2 5
*/

/*
Framgangsmetode:
1) Allokering og deallokering til å fungere
2) Reallokering dersom avsatt minnet er for lite.
*/

//int** 
void allocate_array(int ** p, int row, int col){
   
   int i = 0;
   int j = 0;

   p = (int**)malloc(row * sizeof(*p));   

   for(i=0; i < row; i++){
      p[i] = (int*)malloc(col * sizeof(*(p[i])));
   }

   //return p;
}
/*
void reallocate_array_coloumns(int **p, int row, int new_col){
   for (int i = 0; i < row; i++){
      p[i] = realloc(p[i], new_col * sizeof(*p[i]));
      if (p[i] == NULL){
         printf("Error: could not reallocate new memmory size of %i coloumns to p[%i]", new_col, i);
         return;
      }
      return;
   }
}
*/

void deallocate_array(int ** p, int row){
   
   for (int i = 0; i < row; i++){
      free(p[i]);
      p[i] = NULL;
   }
 
   free(p);
   p = NULL;
}

/*
void initialize_array(int ** p, int row, int col, int multiplier){
   for (int i = 0; i < row; ++i)
   {
      for (int j = 0; j < col; ++j)
      {
         p[i][j] = i*multiplier;
      }
   }
}

/*
void add_sentence_to_array(int ** p, int row, int col, int row_nr){
   snprintf(p[row_nr], col, "Hei");
}*/

/*
void print_array(int ** p, int row, int col){

   for (int i = 0; i < row; ++i)
   {
      for (int j = 0; j < col; ++j)
      {
         printf("%i", p[i][j]);
      }
      printf("\n");
   }
}
*/

int main(){
   int *p;
   
   int row = 3;
   int col = 10;
   int new_col = col*2;
   int multiplier_1 = 1;
   int multiplier_2 = 2;

   printf("allocate_array:\n");
   //p = allocate_array(p, row, col);
   allocate_array(&p, row, col);
/*
   printf("initialize_array:\n");
   initialize_array(p, row, col, multiplier_1);

   printf("print_array:\n");
   print_array(p, row, col);

   printf("reallocate_array_coloumns:\n");
   reallocate_array_coloumns(p, row, new_col);

   printf("initialize_array:\n");
   initialize_array(p, row, new_col, multiplier_2);
   
   //printf("add_sentence:\n");
   //add_sentence_to_array(p, row, col, 2);
   
   printf("print_array:\n");
   print_array(p, row, new_col);
*/
   printf("deallocate_array:\n");
   deallocate_array(p, row);
  
   printf("finish:\n");

   return 0;

}


