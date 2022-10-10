---
files: [add.py, delete.py]
url: https://raw.githubusercontent.com/jsarchibald/cs50/2022/fall/exercises/distro/hello-section/README.md
window: [terminal]
---

# Hello, section

I've taken the liberty of making a small website, [J50](https://j50.herokuapp.com/), that will show photos, names, class years, and present emotional states of anyone who submits! There's a catch, though: to submit, you have to write a Python script to do so.*


*This is not a true statement; you could use other programming languages or even a command-line program if you knew how. But the point of this is to practice Python, so you'll forgive my lying.


## Objectives
- Practice with dictionaries.
- Practice with user input in Python using `get_string` and `get_int`.
- Practice using APIs.


## Getting started

Download the distribution code to your CS50 IDE instance by running the following commands in your IDE terminal:

```
wget https://raw.githubusercontent.com/jsarchibald/cs50/2022/fall/exercises/distro/hello-section.zip

unzip hello-section.zip
```

You'll notice there are three files provided to you! You'll be writing most of `add.py` and `delete.py`. In `lib.py` I wrote some handy helper functions to handle the trickiest parts of the implementation for you:

- **submit** takes in a dictionary mapping specific keys to values that we need for the submission, sends the data to the server, and returns (as an integer) the return status code. If it's anything other than 200, you have a problem.
- **delete** takes in a dictionary mapping only one key, *id*, to an integer with the submission ID to be deleted. It then sends that to the server and returns (as an integer) the return status code. As in **submit**, anything other than 200 is a problem.


## add.py

When you run `python add.py`, the program should ask you for your name, year, current emotional state, and a URL of some picture (to the JPG or PNG itself). It will also read the contents of `add.py` and submit all that data to the server, as by using the **submit** function. If `submit` works (i.e., returns 200) your code should print some congratulatory message -- otherwise, it should tell the user there was an error.


### Specification

1. Create an empty dictionary.
2. Fill in five keys in the dictionary: *name*, *year*, *feeling*, *url*, and *script*. All are strings except *year*, which is an integer. *url* means image URL. *script* means the entire contents of `add.py`, as a string.
3. Use **submit**, something like this: `submit(data)`.
4. Check that **submit** returns 200 - if it does, congratulate the user; otherwise, inform them of an error.


### Hints

- You should write your code in the block of code nested inside `if __name__ === "main":`. That's the main program that will be used when the code is run.
- To initialize an empty dictionary, you can write something like `data = dict()`.
- To access the value associated with a key, e.g. `name`, in a dictionary, you can write something like `data["name"]`.
- To get user input, use the `get_int` or `get_string` functions from the CS50 library for Python. You may need to add a line to the top along the lines of `from cs50 import get_int, get_string`.
- To access the contents of the file in which you're writing your code, you can write this line of code: `with open(__file__) as f:` to open the file. In the block inside that `with` statement, you can then read the entire file's contents as a string by typing `f.read()`.
- You can check that your code works by running it and checking back on the submission site at [https://j50.herokuapp.com](https://j50.herokuapp.com/).


## delete.py

When you run `python delete.py`, the program should ask for the ID of the submission to delete (this can be found on the submissions site). It will submit that ID to the server, and print some message of congratulations if it worked (e.g., returned 200), and some error message otherwise.

### Specification

1. Create a dictionary with just one key: `id`, which maps to an integer submission ID. Bonus points if you do this with `argv` rather than `input`.
2. Use **delete**, something like this: `delete(data)`.
3. Check that **delete** returns 200 - if it does, congratulate the user; otherwise, inform them of an error.


### Hints

- You should write your code in the block of code nested inside `if __name__ === "main":`. That's the main program that will be used when the code is run.
- To initialize an empty dictionary, you can write something like `data = dict()`.
- To access the value associated with a key, e.g. `name`, in a dictionary, you can write something like `data["name"]`.
- To get user input, use the `get_int` function from the CS50 library for Python. You may need to add a line to the top along the lines of `from cs50 import get_int`.
- To use command-line arguments, you'll have to `import sys`. Then, using similar syntax as in C, you can access `sys.argv[index]`, where `index` is some integer.
- You can check that your code works by running it and checking back on the submission site at [https://j50.herokuapp.com](https://j50.herokuapp.com/).
