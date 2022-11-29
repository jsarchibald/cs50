#include <stdbool.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
    if (argc != 3)
    {
        printf("Usage: ./copy infile outfile\n");
        return 1;
    }
    FILE *infile = fopen(argv[1], "r");
    FILE *outfile = fopen(argv[2], "w");
    while (true)
    {
        char c = fgetc(infile);
        if (c == EOF)
        {
            break;
        }
        fputc(c, outfile);
    }
    fclose(infile);
    fclose(outfile);
}
