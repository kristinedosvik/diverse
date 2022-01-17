#include<stdio.h>
#include<string.h>
#include<unistd.h>
#include<errno.h>

int fetchFileContent(char * filename, char * fileContent)
{
    const int buffer_size = 1024;
    char config_file_buffer[buffer_size];
    FILE* config_stream = fopen(filename, "r");
    if (config_stream == NULL)
    {
        printf("Could not open config for reading: %s errno %i: %s", filename, errno, strerror(errno));
        return -1;
    }
    int ret = 0;
    int bytes_read = fread(config_file_buffer, 1, buffer_size, config_stream);
    if (feof(config_stream) == 0)
    {
        printf("Fault reading config %s: Did not reach end of file.", filename);
        ret = -2;
    }
    else if ((ret = ferror(config_stream)) != 0)
    {
        printf("Fault reading config %s: ferror: %i; bytes read: %i", filename, ret, bytes_read);
        ret = -3;
    }
    if (fclose(config_stream) != 0)
    {
        printf("Could not close %s errno: %i", filename, errno);
    }

    strcpy(fileContent, config_file_buffer);
    //printf("FileContent:\n%s\n", fileContent);
    //printf("config_file_buffer:\n%s\n", config_file_buffer);

    return 0;
}

int main(){
	
	char content[1024] = "initial text";
	char * filename = "try.txt";

	fetchFileContent(filename, content);
	//printf("File content:\n%s\n", content);

	return 0;
}
