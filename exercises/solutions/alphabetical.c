#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string text = get_string("Input: ");
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
