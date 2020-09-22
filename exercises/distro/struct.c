#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>


// **
// Create a struct here! Be creative!
// **


int main(int argc, string argv[])
{
    if (argc < 2)
    {
        printf("Usage: ./struct <n>");
        return 1;
    }

    // Assume the user only gives us an integer in the command.
    int n = atoi(argv[1]);

    // **
    // Create an array of structs here, called my_array_of_structs.

    // Don't forget to change the name of the type to match the struct that you made!
    TYPE_NAME_HERE my_array_of_structs[n];

    // **

    for (int i = 0; i < n; i++)
    {
        // Add values to each struct in the array

        // Instead of FIELD_NAME, use the actual fields in your struct!
        // You'll want to use multiple lines like this one to fill in all the data in your struct.
        my_array_of_structs[i].FIELD_NAME = get_string("") // or get_int or get_char or whatever
    }

    for (int i = 0; i < n; i++)
    {
        // Print out each item in the array
        printf("Write something here using %s or %c or %i to describe the data in each element of the array.\n");
    }
}
