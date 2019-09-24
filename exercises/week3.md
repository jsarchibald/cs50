# Week 3 Exercises

Exercises designed by CS50 staff and edited by Josh Archibald for the section of [week 3 of CS50](https://cs50.harvard.edu/college/weeks/3).

Exercises can be completed using [this CS50 Sandbox](http://bit.ly/2mfYLBq).

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

Let's create a program in `struct.c` to populate an array of a struct of your creation. This struct can be anything you want, it just has to take the number of items in the array as a command-line argument and get the input from the user.

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

Josh, 2022, lives in Mather.
Hannah, 2022, lives in Kirkland.
```

### Guiding Questions

- What data do you want to represent in your struct? How can you create that struct?
- Recall from last week how to get command-line arguments and loop through for input. What is different about this problem? What prior knowledge can you apply here?


## Fibonacci

We learned in lecture 3 about recursion. In simple terms, we break down a problem programatically and repeatedly call the same function on an increasingly smaller subset of the problem in order to solve the larger problem at hand.

For example, if we had a series of nodes:

`S -> A -> B -> G`

and wanted to count the number of hops from S to G, we could do this recursively by calling the function on smaller parts of the problem like so:

```c
hops(S -> G) = 1 + hops(A -> G)
             = 1 + 1 + hops(B -> G)
             = 1 + 1 + 1    // assume some logic to know to stop if the node is G
             = 1 + 2
             = 3
```

In this sort of recursive function, we essentially expand out the problem until we can't anymore. At that point, we can start adding the values together.

Let's write a recursive function `fib` within a program `fibonacci.c` to get the `n`th Fibonacci number (where the 0th Fibonacci number is 0, the 1st Fibonacci number is 1, etc.)

Recall that subsequent Fibonacci numbers are the sum of their two predecessors. (So the sequence would look like `0, 1, 1, 2, 3, 5, 8`, etc.)

### Usage

We should be able to run your program like this:

```
./fibonacci 4
3
```

### Guiding Questions

- How will your function know when to stop recursing?
- What special cases might you need to account for?


## Bubble Sort

Sorting algorithms are useful for putting information in order - this could be great if we wanted to do a binary search, for example.

Bubble sort works by swapping elements in an array, as necessary, to order them, moving left to right. The program goes through the array in multiple passes until it knows that the array is in the correct order.

Write a program to bubble sort a user-provided array of integers, then print out the sorted integers. The sandbox gives you some distro code to start with in `bubble.c`.

### Usage

```
./bubble
How many values? 5
Value 0: 2
Value 1: 1
Value 2: 8
Value 3: 4
Value 4: 7
1
2
4
7
8
```

### Guiding Questions

- How can you swap two elements of an array without any data loss?
- How many times do you need to go through the array to be sure it's in order?


## Selection Sort

Selection sort works by finding the smallest element in an unsorted array, swapping it with the element currently in the 0th index of the array, then repeating on the rest of the unsorted array (1st through last indices). For example, given an array  `[2, 1, 8, 4, 7]` the array will look like this over time:

```c
[2, 1, 8, 4, 7]
[1, 2, 8, 4, 7] // 1 is smallest in array so we swap with 2, which was in 0th index
[1, 2, 8, 4, 7] // 2 is smallest in the unsorted array (indices 1-4) so stays the same
[1, 2, 4, 8, 7] // 4 is smallest in the unsorted array (indices 2-4) so swaps with 8, which was in 2nd index
[1, 2, 4, 7, 8] // 7 is smallest in unsorted array (indices 3-4) so swaps with 8, which was in 3rd index
```

Write a program to selection sort a user-provided array of integers, then print out the sorted integers. The sandbox gives you some distro code to start with in `selection.c`.

### Usage

```
./selection
How many values? 5
Value 0: 2
Value 1: 1
Value 2: 8
Value 3: 4
Value 4: 7
1
2
4
7
8
```

### Guiding Questions

- How can you keep track of the minimum value as you loop through the unsorted part of the array?
- How can you keep track of where the unsorted array begins?