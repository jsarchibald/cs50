#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("String: ");

    for (int i = 0, length = strlen(s); i < length; i++)
    {
        printf("%c\n", s[i]);
    }
}
