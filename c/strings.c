#include <stdio.h>

void prints(){
	printf("\nprints:\n");
	//source: https://www.differencebetween.com/difference-between-printf-and-vs-fprintf/
	//source: https://www.geeksforgeeks.org/difference-printf-sprintf-fprintf/
	fprintf(stdout, "fprintf can print formatted strings\n"
			"to files and computer screens.\n"
			"First argument is pointer to where to write to.\n"
			"Second argument is string with formats.\n"
			"Third argument is list of variables.\n"
			"List of arguments: %d, %c.\n\n",
			100, 'K');

	printf("printf is the same as fprintf, but it only prints to\n"
			"the standard output stream, which is the\n"
			"computer screen.\n\n");

	char buffer[160];
	sprintf(buffer, "sprintf is the same as fprintf but store\n"
			"the result in the char array which is the first\n"
			"argument. If the char array is to smal we get\n"
			"core dumpe error.\n\n");
	printf("%s", buffer);
	
	char buffer2[350];
	int size = 350;
	snprintf(buffer2, size, "snprintf is the same as sprintf, but we\n"
			"specify the number of byte we write to buffer2\n"
			"in variable size=%d. If the size is less then the\n"
			"buffer, only the first size-1 chars are written.\n"
			"The last char is some terminating char (?)\n"
			"If char variable is too small (and smaller than size)\n"
		        "we get core dump error.\n\n",
			size);
	printf("%s", buffer2);

	printf("Ekstra information:\n"
			"Every lineshift in the code (not \\n ) needs new quote marks \".\n"
			"String denotes with doble quote marks \", while char with single quote marks \'.\n\n");

}

void integerToString(){
	printf("\nintegerToString:\n");
	//Integer is 2 to 4 bytes: max number = +/-2 147 483 647, which gives max size = 10. +1 for sign, +1 for '\0' (?)
	//max number gives = str = ['+/-', '2', '1', '4', '7', '4', '8', '3', '6', '4', '7', '\0'] 
	//Too little size gives core dump (memory overwriting).
	int size = 12; 

	int integer = 10203;
	char str[size]; 

	//Turn integer to string
	sprintf(str, "%d", integer);
	
	//check results:
	printf("integer = 	%d\n", integer);
	printf("str = 		%s\n\n", str);
	
	return;
}

int main(){
	prints();
	integerToString();
	
	return 0;
}
