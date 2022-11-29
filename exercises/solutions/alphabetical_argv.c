#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// ./alphabet_argv abcdef

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./alphabet_argv <string>\n");
        return 1;
    }

    string text = argv[1];
    int length = strlen(text);

    for (int i = 1; i < length; i++)
    {
        if (text[i] < text[i - 1])
        {
            printf("No\n");
            return 0;
        }
    }
    printf("Yes\n");
}