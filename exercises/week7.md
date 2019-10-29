# Week 7 Exercises

Exercises designed by CS50 staff and edited by Josh Archibald for the section of [week 7 of CS50](https://cs50.harvard.edu/college/weeks/7).

Exercises can be completed using [this CS50 Sandbox](http://bit.ly/2qO6Y25).

This week's exercise is really a bunch of smaller tasks related to one database.

## Create a database

Create a new database in a file called `students.db`.

## Create tables

Create tables to represent:

### People

- id
- name

### Courses

- id
- code
- title

### Students

- person_id
- course_id

### Instructors

- person_id
- course_id

## Add data

Add some people to this database. (The full data import will be copied and pasted.)

## Some questions you can now answer

- What is Alice's student id?
- What is the course title for CS51?
- What are the course codes and titles for all CS courses?
- How many courses are there?
- How many students are taking CS50?
- What are the names of all the instructors?
- What are the names of all the students taking CS50?

## Update the database

- Alice wants to switch from CS50 to CS51.
- CS182 was cancelled.

## Scripting

Write a Python program `enroll.py` that adds new students to the roster and enrolls them in courses.
