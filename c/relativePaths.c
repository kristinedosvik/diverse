#include<stdio.h>
#include<unistd.h>
#include<libgen.h>


void pathName(char* path)
{
	if( access( path, F_OK ) == 0 ) {
		char cwd[1000];
		getcwd(cwd, sizeof(cwd));
		printf("file exist: %s/" __FILE__ "\n", cwd);
		char* paths = dirname(cwd); //[1000] = "";
		sprintf(paths, "%s%s", "hh", paths); //dirname(path));
		printf("paths = %s\n", paths);
	}
	else
	{
		
		printf("file does not exist\n");
	}

}

int main()
{
	char path[50] = "mkdir.c";
	pathName(path);

	return 0;
}
