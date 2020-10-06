# Week 5 Exercises

Exercises designed by CS50 staff and edited by Josh Archibald for the section of [week 5 of CS50](https://cs50.harvard.edu/college/2020/fall/weeks/5).

Exercises can be completed using the CS50 IDE.


## Linked Lists

Recall from lecture that a linked list allows us to store as many elements in a list-style data structure as we want. This is different than arrays, which in C have a fixed length. Let's implement a linked list in `list.c` such that user-inputted integers are added to the head of the list. (This means they should print out in reverse order from their input order.)

The distribution code is broken down into smaller parts for you to solve:

1. Allocate a new node.
2. Add new node to head of linked list.
3. Print all nodes of linked list.
4. Free all nodes from memory. (This should give you a hint as to how to implement #1!)


### Getting started

Download the distribution code in the CS50 IDE by running this command:

`wget https://raw.githubusercontent.com/jsarchibald/cs50/2020/fall/exercises/distro/list.c`

### Guiding questions

- What does the `node` struct do? What is its structure?
- What in the `node` struct allows us to create a linked list, a series of interconnected `node`s?
- How can we add a `node` to the head, or beginning, of a linked list by taking advantage of the `node` struct?

## Linked Lists - In Order

The linked list you just implemented stores integers in the reverse order of their input. For example, if you input 1,2,3 then the linked list implementation above will store them as 3,2,1.

Now implement a linked list in `listrev.c` such that the integers are stored in the order of their input. Modify your code from `list.c` to do this.

### Guiding questions

- What do we need to do to add a `node` to the end of a linked list?
- What is the time complexity (big-O notation) of this linked list implementation?

## Linked Lists - Sorted

Now modify your code such that `listasc.c` will store the integers in ascending order within a linked list.

### Guiding questions

- How can we compare the inputted number to the numbers that already exist in the linked list?
- How can we make sure we don't lose any data in our implementation? In other words, how do we make sure that if we have to place a new `node` between two existing nodes, all the nodes will point to each other in the appropriate order?
