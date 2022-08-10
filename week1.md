# Week 1: C

Slides

[Exercises](exercises/week1.md)

Exercise solutions


## Extra resources

[Video on data types](https://www.youtube.com/embed/q6K8KMqt8wQ?rel=0&showinfo=0)

[Video on operators](https://www.youtube.com/embed/7apBtlEkJzk?rel=0&showinfo=0)

[Video on conditional statements](https://www.youtube.com/embed/FqUeHzvci10?rel=0&showinfo=0)

[Video on loops](https://www.youtube.com/embed/QOvo-xFL9II?rel=0&showinfo=0)

[Video on the command line](https://www.youtube.com/embed/lnYKOnz9ln8?rel=0&showinfo=0)

[Video on debugging](https://www.youtube.com/watch?v=w4TAY2HPLEg)


## FAQs

### Linux commands

`ls` will list all the files/subdirectories in your current directory.

`cd DIRECTORY` will change current folder location to the `DIRECTORY` of your choosing.

`cd ..` will go back one directory. (So if we're in `code/pset1` then running `cd ..` will bring us back to `code`.)

`rm FILE` will remove the file `FILE`.

`mkdir DIRECTORY` will create the folder `DIRECTORY`.


### What's the difference between for, while, and do-while loops?

[This](https://stackoverflow.com/a/2950945/6062385) is a pretty good answer I found on the internet that goes into a fair amount of detail. In particular, here's a nice quick excerpt that wraps it up nicely:

> The main difference between the `for`'s and the `while`'s is a matter of pragmatics: we usually use `for` when there is a known number of iterations, and use `while` constructs when the number of iterations in not known in advance. The `while` vs `do ... while` issue is also of pragmatics, the second executes the instructions once at start, and afterwards it behaves just like the simple `while`.

Basically, we typically use `for` loops when we know the number of times something should happen. Otherwise, we use `while`. And in cases where `while` is sufficient but  we want to always do the thing inside the loop at least once, we use a `do-while`.

There are some cases where you could use several of these loops, but it comes down to code design choices that you'll gain an intuition for as you get more experience programming. Not to worry if these design decisions don't seem quite obvious as of yet; I'm happy to help you throughout the semester (and will leave feedback on your psets as well).


### I'm having trouble compiling my code. Help!

First, make sure your *terminal* is in the folder where your code is located! For example, if you put your code for section inside a folder called `section`, use the command `cd section` in your terminal to **c**hange **d**irectory to the `section` folder.

Second, make sure you're calling `make mario`, not `make mario.c`, for example. Our setup of `make` doesn't like file extensions!

Still having trouble? Try putting `help50` in front of the word `make` and run that new command. If there's an actual compilation error, it'll help you figure that out.

If all that doesn't work, go to tutorial or email your TF!

#### Tips for navigating the file system in the terminal

If you're not sure where you are in your terminal's file system, you can find out the answer to the left of the `$` in the terminal -- `~/` means home folder. So if you're in the `section` folder inside your home folder, you should see `~/sections/` to the left of the `$`.

If you ever get completely lost, `cd ~` will bring you back to your home folder.

Many people find it useful to see the folders and files in their current directory when they're navigating. Type `ls` in your terminal to **l**i**s**t the contents of the folder you're currently in.

- For example, when I start my IDE, I often forget what exactly I called the folder where I store my section code. So I run `ls`, see that it's `sections`, and then run `cd sections`. To verify that I'm there, I can run `ls` again and all my section code is listed.
