# Week 4 Exercises

Exercises designed by CS50 staff and edited by Josh Archibald for the section of [week 4 of CS50](https://cs50.harvard.edu/college/weeks/4).

Exercises can be completed using [this CS50 Sandbox](http://bit.ly/2mxBCLD).

## Malloc and free

Recall that we can dynamically allocate memory using `malloc` and free that memory using `free`. Let's get some practice, over the next five minutes or so, in doing just that.

In `malloc.c` there are two comments indicating where you should write the following two tasks.

1. Allocate space for an integer. Assign an integer value to that space in memory. Print out the value, then free the memory.
2. Allocate space for a string. Assign a string value to that space in memory. Change the first character to some value (maybe uppercasing it if you're feeling ambitious?), then free the memory.

### Guiding questions

- What is the syntax of `malloc`? What is the syntax of `free`? What arguments do each take?
- How can we dereference, or follow, a pointer to its value?

## Concatenate

Write a program that takes two strings, `s1` and `s2`, and returns one combined string. For example, `concatenate("hello ", "world");` should return `hello world`. I've provided you with distribution code in `concatenate.c` to get the two strings; you just need to write the `concatenate` function.

### Guiding questions

- Why can't we just add the strings, as with `s1 + s2`?
- How would we copy one string?
- How can we make sure our output is a valid string? (Hint: think of what character terminates every string in C.)

## Copy

Write a program `copy.c` that copies `file1` to `file2`. (We'll do this one together to get practice with file pointers.)

### Usage

```
./copy file1 file2
```

Should create `file2` with the same contents as `file1`.

### Guiding questions

- How can we go through every character of file1?
- What functions can we use to read and write a single character from a file stream?

## Uppercase

Write a program `uppercase.c` with your partner that does the same thing as in `copy.c`, but which also makes every alphabetical character an uppercase English letter.

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
- How can we update

## GIF Detection

Write a program `gif.c` that checks if a file is (likely) a GIF (specifically, a GIF 89a file, the latest version of the GIF file format). Note that the first six characters of a GIF 89a file are the characters `G, I, F,  8, 9, a`.

I've provided some distribution code in `gif.c` to handle all the command-line arguments, so you just need to implement `is_gif`. There's a sample GIF (which is valid) in `cat.gif`. (You should also try checking if some other file in the sandbox is *not* a valid GIF.)

### Usage

```
./gif cat.gif
GIF
```

### Guiding questions

- What part of the file do we want to read and check?
- How can we check that part of the file against what we know will be the first 6 characters of a GIF 89a file?
