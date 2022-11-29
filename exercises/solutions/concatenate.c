#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *concatenate(char *s1, char *s2);

int main(void)
{
    char *s1 = get_string("s1: ");
    char *s2 = get_string("s2: ");

    char *s3 = concatenate(s1, s2);
    printf("%s\n", s3);
    free(s3);
}

char *concatenate(char *s1, char *s2)
{
    int size_1 = strlen(s1);
    int size_2 = strlen(s2);

    char *s3 = malloc(size_1 + size_2 + 1);

    for (int i = 0; i < size_1; i++)
    {
        s3[i] = s1[i];
    }

    for (int i = 0; i < size_2; i++)
    {
        s3[i + size_1] = s2[i];
    }

    s3[size_1 + size_2] = '\0';

    return s3;
}
