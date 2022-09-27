#include <stdio.h>
#include <stdlib.h>

/*
Peker på peker
_______
|     |
|  a  |
|_____|0x0
|p*:  |
| 0x0 |
|_____|0x4
|p**: |
| 0x4 |
|_____|0x8
|     |
|     |
|_____|0x12
|     |
|     |
|_____|0x16

Minne plassert i kategorier:
__________
|_c1_|____|_________
|_c2_|____|____|____|
|_c3_|_________
|_c4_|____|____|
|_c5_|

*/

/*



Designspesifikasjoner:

INTERAKSJON:

- Bruker spør om en dagsmeny/ingrediensliste
- Dagsmenyene som genereres skal ha et krav om viss mengde ulike typer i løpet av en viss tid:
 * proteiner
 * mineraler
 * vitaminer
 * karbohydrater
 * kostfiber
 * umettet fett
 * flerumettet fett
 * omega-3
 * omega-6
 * osv.

- Man skal kunne skrive inn ulike ting man har spist og få tracket hva man har spist
 * Da får man opp mengden næringstoffer man har fått i seg
 * Det inkluderer advarsel om hvilke uheldige stoffer vi har fått i oss
 * Dette kan være en av dagsmenyene

- Man ønsker en viss type fordeling av mengden næringsstoffer
 * Etterhvert vil man sette opp matplaner slik at denne fordelingen opprettholdes til størst mulig grad

- Dagsmenyen skal gi en advarsel over hvor stor mengde det er av
 * mettet fett
 * E stoffer
 * Andre prosesseringsstoffer

- Det skal genereres flere ulike dagsmenyer slik at man har valgmuligheter
 * Menyene skal rates utifra hvor god kombinasjon de er i forhold til det som allerede er spist

- Man skal kunne sette opp krav til at menyene inneholder visse ingrediens, eller utelukker en visse ingredienser

- Hvor stor mengde av hver ingrediens porsjon skal være med

- Man kan se oversikt over hvilke næringsstoffer man mangler, og få opp ingredienser som inneholder dette næringsstoffet sortert etter mengde per gram

DATAOPPSETT:

- Legge til ingrediens (legge til en tekstfil)
 * Utvide tabellen over næringsstoffer etterhvert som næringsstoffer blir oppdaget
- Lagre ingrediensliste (i tekst-fil format)
- Sortering i forhold til ulike typer næringstoffer (lagres i vektorformat)
- Oversikt over fordelingen mellom de ulike type næringsstoffene (lagres som prosentandeler av hvilken mat jeg får i meg)
- Lagre næringsstoff med 1 enhets-verdier (så si hva typisk 1 posjon vil bidra med)


Utviklingsplan:
1) 
2) 

*/

void make_category(){

   return 
}

int main(){
   int *p;
   
  
   printf("finish:\n");

   return 0;

}
