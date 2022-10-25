#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int total = 0;

    for (int i = 0; i < 10; i++)
    {
        total += get_int("Number: ");
    }

    printf("The sum is %d\n", total);
}
