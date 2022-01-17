#include <stdio.h>
#include <stdlib.h>

int main () {
   char str[30] = " -000"; // This is test"; //string must start with the number, can have spaces or zeroes infront of the number, but not a char value.
   char *ptr; //Holds the rest of the string that comes after the number, can have NULL if this part is not interesting.
   int ret; //the value, zero if errors
   int base = 10; //10 --> return results as desimal number.

   ret = strtol(str, &ptr, base); //convert long to int
   printf("The number(unsigned long integer) is %d\n", ret);
   printf("String part is |%s|\n", ptr);

   if(*ptr != '\0'){
	printf("more than integers\n");
   }else{
	printf("only integers\n");
   }

   return(0);
}
