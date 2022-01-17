#include<stdio.h>
#include<string.h>

int main()
{
        char *p="Hei, dette er en test.\n"
		"Det er kun et forsok på å sjekke om\n"
		"funksjonen fetchFileContent fungerer.\n"
		"// og for å se om den tar bort kommentarer\n"
		":-)\n"
		"/* Det hadde isåfall vært nice,\n"
		"tenker// jeg!\n"
		"Gjør ikke du også det?*/\n"
		"Eller?\n";

        
	char temp[512];
	char* lineComment;
	char* nextLine;
 
        char newText[2000] = "";

	int dif;

	printf("Original text:\n%s", p);
        
	while ( (lineComment = strstr(p, "//")) != NULL ){

		//add content:
                dif = (int)(lineComment - p);
		snprintf(temp, dif+1, "%s", p); //+1 because adds '\0'
		

		//find next line:
		nextLine = strstr(lineComment, "\n");
		p = nextLine+1;

                strcat(newText, temp);
        }
	
	//add the rest of the uncomment content:
	strcat(newText, p);	

	printf("newText:\n%s", newText);

        return 0;
}
