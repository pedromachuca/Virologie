//Compilation : gcc -O3 -Wall -W -Wstrict-prototypes -Werror virusC.c _o virusC
//Utilisé pour enlever les erreurs et avoir une meilleure compilation.

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){

	char cmd[40];	
	printf("### Virus name : %s\n", argv[0]);
	if(argc ==2){
		printf("### Copy virus in %s\n", argv[1]);	
		sprintf(cmd, "cp %s %s", argv[0], argv[1]);
		system(cmd);
	}
	return 0;
}
