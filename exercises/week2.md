# Week 2 Exercises

Exercises designed by Joshua Archibald (and CS50 staff) for the section of [week 2 of CS50](https://cs50.harvard.edu/college/weeks/2).

Exercises can be completed using [this CS50 Sandbox](http://bit.ly/2UOBF2i).

## Introductions

Most likely, most of us here don't know each other's names! Since we'll be getting to know each other over the course of the semester, it would be really great if we could start to learn each other's names.

Why don't we try implementing a program that will take everyone's name as an input, then greet us individually?

### Usage

Our program should behave something like this when it's done:

```
$ ./intros 3
Hi there, what's your name? Josh
Hi there, what's your name? Fernando
Hi there, what's your name? Felipe

Hello, Josh!
Hello, Fernando!
Hello, Felipe!
```

### Guiding Questions

- How can we get what is called a **command-line argument** in C? This problem asks us to get a number of people when we run the command. How do we retrieve that number?
- What type of loop might we want to use to get the right number of names?
- What functions in `cs50.h` can we use to get user input? What kind of input do we need to complete this problem?


## Longest Name

Let's say we want to figure out who has the longest name based on the names we're getting in `intros.c`.

How could we use some of the code from `intros.c`, and then add some new code, to implement such a program?

### Usage

Our program should behave something like this when it's done:

```
$ ./longest 3
Hi there, what's your name? Josh
Hi there, what's your name? Fernando
Hi there, what's your name? Felipe

Fernando has the longest name, at 8 characters!
```

### Guiding Questions

- What parts of `intros.c` can we just reuse in this program?
- How might we count the number of characters in a string?
- How can we keep track of who has the longest name?
- How can we keep track of the length of the longest name?
- What should we do if multiple people are tied for longest name? (For the purposes of this exercise, just return the first name of that length. But think about some other solutions.)

### Stretch Questions

- How might we change the code we wrote to find the **shortest** name?
- How might we change the code we wrote to print out every name with a length greater than an integer *n*?

## First Letters

Maybe, just for fun, we want to see how many times a letter appears as the first letter in someone's name.

Let's write a program with similar functionality to those we've already implemented, but which tells us the number of times each letter starts a name. Crucially, it should only report a letter's count if at least one name starts with that letter.

### Usage

Our program should behave something like this when it's done:

```
$ ./letters 3
Hi there, what's your name? Josh
Hi there, what's your name? Fernando
Hi there, what's your name? Felipe

F starts 2 names.
J starts 1 name.
```

### Guiding Questions

- What parts of the code can we reuse from `intros.c` or `longest.c`?
- How might we keep track of the number of times each letter starts a name?
- How can we access the first character of a string?
- How can we make sure we only report the number of times a letter appears if it appears at least once?
- How can we make the program decide whether to print out `name` or `names`?


## Initials

As a final exercise, let's write a program `initials.c` that takes a user's full name as input, and outputs their initials.

- The program should accept a user's name using get_string
- Initials should all be printed as uppercase letters, even if the name contains lowercase letters
- Students can assume that the user's names will be separated by one space

### Usage

Our program should function something like this:
```
$ ./initials
Name: John W. Oliver
JWO
```

### Guiding Questions

- What concepts can we apply from `intros.c`, `longest.c`, and `letters.c` -- and if any, what code can we reuse -- to solve this problem?
- How can we decide whether to print out a character as an initial?