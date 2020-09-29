# Week 4 Exercises

Exercises designed by CS50 staff and edited by Josh Archibald for the section of [week 4 of CS50](https://cs50.harvard.edu/college/2020/fall/weeks/4).

Exercises can be completed using the CS50 IDE.

## Malloc and free

Recall that we can dynamically allocate memory using `malloc` and free that memory using `free`. Let's get some practice, over the next five minutes or so, in doing just that.

In `malloc.c` there are two comments indicating where you should write the following two tasks.

Allocate space for an integer. Assign an integer value to that space in memory. Print out the value, then free the memory.

How about allocating the space for two integers?

### Guiding questions

- What is the syntax of `malloc`? What is the syntax of `free`? What arguments do each take?
- How can we dereference, or follow, a pointer to its value?


## Concatenate

Write a program that takes two strings, `s1` and `s2`, and returns one combined string. For example, `concatenate("hello ", "world");` should return `hello world`. I've provided you with distribution code in `concatenate.c` to get the two strings; you just need to write the `concatenate` function.

### Getting started

Download the distribution code in the CS50 IDE by running this command:

`wget https://raw.githubusercontent.com/jsarchibald/cs50/2020/fall/exercises/distro/concatenate.c`

### Guiding questions

- Why can't we just add the strings, as with `s1 + s2`?
- How would we copy one string?
- How can we make sure our output is a valid string? (Hint: think of what character terminates every string in C.)


## Copy

Write a program `copy.c` that copies `file1` to `file2`. (We'll do this one together to get practice with file I/O.)

### Usage

```
./copy file1 file2
```

Should create `file2` with the same contents as `file1`.

### Getting started

Create a file called `copy.c` in the CS50 IDE.

### Guiding questions

- How can we go through every character of file1?
- What functions can we use to read and write a single character from a file stream?


## Uppercase

Write a program `uppercase.c` that does the same thing as in `copy.c`, but which also makes every alphabetical character an uppercase English letter.

### Usage

```
./uppercase file1 file2
```

If `file1` contains:

```
Explore Lands of Endless Enchantment, Where Your Fantasy Becomes a Reality
```

Then `file2` should contain:

```
EXPLORE LANDS OF ENDLESS ENCHANTMENT, WHERE YOUR FANTASY BECOMES A REALITY
```

### Guiding questions

- What code can we reuse from `copy.c`?
- What function can we use to uppercase alphabetic characters?
