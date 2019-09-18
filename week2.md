# Week 2: Arrays

[Slides](https://docs.google.com/presentation/d/1-MHtC9RO_by55RYC93tXcMrCFGDlo1r2FYukHna7p6s/edit?usp=sharing)

[CS50 Sandbox](http://bit.ly/2UOBF2i)

[Exercises](exercises/week2.md)

[Exercise solutions](http://bit.ly/3089l0z)

[Attendance](https://forms.cs50.io/5d5b44df-3268-4585-b49e-7d36c178e71f)


## Extra resources

[Video on arrays](https://www.youtube.com/watch?v=mISkNAfWl8k)

[Video on functions](https://www.youtube.com/watch?v=b7-0sb-DV84)

[Video on the command line](https://www.youtube.com/watch?v=thL7ILwRNMM)

[Video on debugging](https://www.youtube.com/watch?v=w4TAY2HPLEg)


## FAQs

From the form y'all submitted before section.


### Linux commands

`ls` will list all the files/subdirectories in your current directory.

`cd DIRECTORY` will change folders to the `DIRECTORY` of your choosing.

`cd ..` will go back one directory. (So if we're in `code/pset1` then running `cd ..` will bring us back to `code`.)

`rm FILE` will remove the file `FILE`.

`mkdir DIRECTORY` will create the folder `DIRECTORY`.


### Command-line arguments

- `argc` gives us the total argument count when a program is run.
- `argv` is an array of the strings that are the arguments the program is run with.
- `argc` and `argv` do count the program name as an argument. So `make mario` has two arguments, as far as the C programming language is concerned.


### What is the purpose of a return value?

For many functions, we expect to receive some sort of output for our input.

For example, if we were to write a function to square an integer, we expect to input an integer and get an integer from the function. This function might look something like this:

```c
int square(int i)
{
    return i * i;
}

```

- The first `int` in the function signature indicates the output type of our function, in this case an integer.
- The word `square` is the name of the function.
- The inputs to the function go inside the parentheses. We see here that there's only one input, an `int` variable with the name `i`.

So return values have a very practical purpose with functions like this. **But why, you ask, do we have a return value for main?**

Recall that we, by convention, start the main function (the main program) something like this:

```c
int main(void)
{
    ...
}
```

Going on the same logic as we used with `square`, we see that the `int` in the signature means we have to return an integer. This is a convention in C. So we need to return an integer, since we're expecting an integer output from `main`. Make sense?

Usually, if everything goes well in the program, we'll `return 0`. This means nothing seems to have gone wrong in the execution of our code. But if something goes wrong, we can use the return values kind of like error codes. For example, `return 1` might indicate a problem with the command-line arguments, and `return 2` might mean we weren't sure how to handle a particular user input. These codes can be used by the command line shell to figure out where exactly a program's execution went wrong.

There's a more succinct version of this explanation that may help clarify some more, if you're still confused, [here](https://www.codeproject.com/Answers/693052/why-do-we-have-to-use-return-0#answer3) (just ignore the sentence about C++).


### Design questions

Most questions about pset 1 were related to design - sign up for a code review for details on the design optimizations of previous psets. We won't (for the most part) discuss the design of past pset solutions in section for time constraints.


### Pset strategy questions

A few of you asked about how to best approach psets, since it seems like there's a lot of debugging involved.

The fact is programming *is* debugging. Many of your hours will go into fixing buggy code, and that's okay! That's how we learn and improve, and even professionals who have worked in industry for many years still sometimes write buggy code. The key thing is to develop strategies for debugging and getting the code working.

In terms of pset strategy, it may be helpful to first think in pseudocode about how you'd solve the problem, draw diagrams or otherwise visualize the problem, break down the problem into smaller parts, then implement and debug one part at a time.