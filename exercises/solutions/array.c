#include <stdio.h>

int main(void)
{
    // Constant -- the size of the array
    const int SIZE = 5;

    // Initializing the array
    int numbers[SIZE];
    numbers[0] = 1;

    // Populate the array with values 2 times the previous number
    for (int i = 1; i < SIZE; i++)
    {
        numbers[i] = numbers[i - 1] * 2;
    }

    // Print out the array
    for (int i = 0; i < SIZE; i++)
    {
        printf("%i\n", numbers[i]);
    }
}
