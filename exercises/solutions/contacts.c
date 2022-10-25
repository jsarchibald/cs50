#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt the user for name, age, phone number
    string name = get_string("What's the name? ");
    int age = get_int("What's the age? ");
    string phone = get_string("What's the phone number? ");

    // Print things out
    printf("%s, age %i, can be reached at %s\n", name, age, phone);
}
