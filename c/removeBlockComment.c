#include<stdio.h>
#include<string.h>

int main()
{
        char *p="Hei, dette er en test.\n"
                "Det er kun et forsok på å sjekke om\n"
                "funksjonen /*fetchFileContent*/ fungerer.\n"
                "// og for å se om den tar bort kommentarer\n"
                ":-)\n"
                "/* Det hadde isåfall vært nice,\n"
                "tenker// jeg!\n"
                "Gjør ikke du også det?*/\n"
                "Eller?\n";


        char temp[512];
        char* commentStart;
        char* commentEnd;

        char newText[2000] = "";

        int dif; 

        while ( (commentStart = strstr(p, "/*")) != NULL ){
                
                //add content: 
                dif = (int)(commentStart - p);
                snprintf(temp, dif+1, "%s", p); //+1 because adds '\0'
                
                
                //find next valid input:
                commentEnd = strstr(commentStart, "*/");
                p = commentEnd+2; 
        
                strcat(newText, temp);
        }

        //add the rest of the uncomment content:
        strcat(newText, p);

        return 0;
}

