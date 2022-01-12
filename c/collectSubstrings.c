#include<stdio.h>
#include<string.h>

int main()
{
	char *p="par.l.par.--.par.123.";
	char *p2;
	char *p_end=".";
	char *substring = "par.";
	int total=0;
	char x[15] = "";
	char temp[15] = "";
	int dif;
	while ( (p=strstr(p,substring)) != NULL ){
		
		p2 = strstr(p+strlen(substring), p_end);
		
		dif = (int)(p2 - p) - strlen(substring);
		printf("dif = %d\n", dif);

		//write new cars to temp
		snprintf(temp, dif+1, "%s", (p+strlen(substring))); //+1 because adds '\0'
		//add new chars to x
		strcat(x, temp);

		printf("|temp = %s\n", temp);
		printf("|x = %s\n", x);
		
		total++;
		p++;
		
	}
	printf("num substrigs = %i \n", total);

	return 0;

}
