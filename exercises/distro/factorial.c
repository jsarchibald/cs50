#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

int factorial(int n);


// You shouldn't have to change main!
int main(int argc, string argv[])
{
    // Check for command line argument.
    if (argc < 2)
    {
        printf("Usage: ./factorial <n>");
        return 1;
    }

    // Assume the user only gives us an integer in the command.
    int n = atoi(argv[1]);

    // Get the factorial.
    int f = factorial(n);


    printf("%i! = %i\n", n, f);
}
