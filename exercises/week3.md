# Week 3 Exercises

Exercises designed by CS50 staff and edited by Josh Archibald for the section of [week 3 of CS50](https://cs50.harvard.edu/college/2020/fall/weeks/3/).

Exercises can be completed using the CS50 IDE.

## Structs

As we saw in lecture, we can use structs to develop richer data types than the builtin types C gives us (like `int` or `float`). For example, we can use a struct to define a new type `student`:

```c
typedef struct
{
    string name;
    int year;
    string house;
}
student;
```

We can then create new variables using the `student` type:

```c
student josh;

josh.name = "Josh";
josh.year = 2022;
josh.house = "Mather";
```

We can even create an array of students!

```c
student students[2];

students[0].name = "Josh";
students[0].year = 2022;
students[0].house = "Mather";
```

Let's create a program in `struct.c` to populate an array of a struct of your creation. This struct can be anything you want. I already wrote the loops for you, you just need to write the code to (a) create the struct, (b) fill up each struct with data, and (c) print out the data from each item in the array.

### Usage

An example with students may behave something like this:

```
./struct 2

Name: Josh
Year: 2022
House: Mather

Name: Hannah
Year: 2022
House: Kirkland

Josh, 2022, would normally live in Mather.
Hannah, 2022, would normally live in Kirkland.
```

### Guiding Questions

- What data do you want to represent in your struct? How can you create that struct?
- How can you print out data from a struct?


## Factorial

Write a recursive function `factorial` that takes an integer `n` and computes its factorial. (The factorial of 5, for example, is 5 * 4 * 3 * 2 * 1 = 120).

Distro code is in `factorial.c`. The only rule is that you can't use any loops.

### Guiding Questions

- What does it mean for a function to be recursive?
