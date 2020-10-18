# Week 7 Exercises

Exercises designed by Josh Archibald for the section of [week 7 of CS50](https://cs50.harvard.edu/college/2020/fall/weeks/7).

Exercises can be completed using the CS50 IDE.


## My Cabbages!

I feel reasonably comfortable saying that I'm not the only one here who watched *Avatar: The Last Airbender* while quarantining this summer. In fact, two of you made Avatar-themed Scratch projects for pset 0!

For those who haven't watched, there is a running gag in the show involving a cabbage merchant whose produce tends to be destroyed when in close proximity to the show's protagonists. Here is a clip from the cabbage man's first tragic appearance:

https://youtu.be/GrobFjIRRCc

Today, we will be helping the cabbage man to organize his cabbages with a SQL database. Let's get started!


### 0. Open the CS50 IDE.

Navigate in the terminal to the directory where you want to do your work using `cd` and `mkdir` as needed.


### 1. Create a database.

As it turns out, creating a SQLite database on a Linux computer (like the CS50 IDE) is pretty simple. The `touch` command will create any file you specify. For example, `touch cabbages.db` will create an empty file in the current working directory called `cabbages.db`. Keep in mind that although we're using this command to create an empty `.db` file in this case, you could use it to create empty Python, C, or any other type of empty file as well.

#### Before moving on
- Did you create a new file ending in `.db` in which to store the database?


### 2. Open the database in SQLite.

SQLite happens to be the specific *dialect* of SQL that we're working with right now. We're using SQLite because it uses a single file, e.g. `cabbages.db`, to store all its data. Other types of SQL databases, like MySQL or PostgreSQL, are a little more complicated in terms of setup, so we ignore them for now.

SQLite has a handy command-line program we can use to work with databases (kind of like how Python has a program we can use to experiment with individual lines of Python). To open up our new cabbage database, we can run: `sqlite3 cabbages.db`. This starts the SQLite program that lets us run SQL code.

#### Before moving on
- Did you open `cabbages.db` in the SQLite command-line program?


### 3. Create some tables.

Let's get this database started! Cabbage Man is hoping to have three tables to get off the ground:

- customers
  - id
  - name
  - email
- invoices
  - id
  - customer_id
  - total_value
- cabbages
  - id
  - type
  - batch_id
  - invoice_id
  - value

From this we know what the *schema* of the database should look like. Now we just have to write the actual SQL to make it happen.

How do we come up with that SQL? Ok, first it's important to acknowledge: most software engineers don't necessarily remember every syntax they need to use. What's more important than memorizing syntax? Figuring out what you don't know, and knowing how to find the resources to learn.

In my case, SQL tends to slip through the cracks, especially the syntax for creating tables (which I don't actually do very much). So it's good to find some resources that will help you figure it out. For anything related to the internet, including SQL and HTML, CSS, and JavaScript (next week's material!) I like to use a site called [W3Schools](https://www.w3schools.com).

To come up with the syntax to create the tables above, we may find [this page on W3Schools](https://www.w3schools.com/sql/sql_create_table.asp) helpful. Reading through that page, we see that the general syntax looks something like:

```sql
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
   ....
);
```

So for each column we just need to know what we want to call it and the type it should be (along with any special parameters to go with it, which we'll see below).

Let's create the `customers` table together:

```sql
CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
);
```

So, we're creating a table called `customers`. This table has three columns: an `id`, which is the "Primary Key" of the table and is set to start at 1 and increase automatically whenever we insert rows (`AUTOINCREMENT`). A name, which is a `TEXT` field and must have a value (`NOT NULL`), and an email, which has the same type and requirement as the name.

Cool! We now have a customers table. Go ahead and use similar syntax to create the `invoices` and `cabbages` tables, making sure to match the schemas defined at the top of this section.

#### Before moving on
- Did you create the `invoices` and `cabbages` tables according to the spec above?


### 4. Inserting some data into the database.

Fantastic, now we have three tables -- `cabbages`, `customers`, and `invoices` and can start to populate our database with some actual data. Just to practice inserting data, we're going to add some `customers` to the database.

As with `CREATE TABLE`, we can look to W3Schools for a good-quality syntax reference of `INSERT INTO` [here](https://www.w3schools.com/sql/sql_insert.asp).

Let's say I want to add a customer named Aang to the database. Using the `INSERT INTO` syntax, I can just write something like this:

```sql
INSERT INTO customers (name, email) VALUES ("Aang", "aang@team.avatar");
```

So I'm saying here that I want to insert a row into the `customers` table, with the `name = "Aang"` and the `email = "aang@team.avatar"`. The first tuple (the stuff inside parentheses) tells SQL the order of the columns for which I'm giving it values; the second tells SQL the corresponding values to put in each column for this new row. So by putting `name` first in the first tuple, I'm saying that the first value I provide -- `Aang` -- should go into the `name` column.

Ok, go ahead and practice this syntax by inserting any two of the following customers into the database:

| Name         | Email                      |
|--------------|----------------------------|
| Iroh         | iroh@fire.gov              |
| Katara       | katara@team.avatar         |
| Sokka        | sokka@team.avatar          |
| Toph         | toph@team.avatar           |
| Zuko         | zuko@fire.gov              |


#### Before moving on
- Did you add two of those people into the customers database?

#### Check your work

I made a check50 for this first part of our work with the cabbage merchant!

First, close out of the SQLite command-line program by pressing `CTRL-D`.

Then, run this in your terminal to check your answers:

```
check50 jsarchibald/cs50/2020/fall/exercises/7/start
```


### 5a. Simulate some cabbage purchases.

Okay, we now have our database schema set up and have practiced some insertions. Now let's do the heavy lifting of adding a bunch of data. It's actually heavy lifting I did for you -- you just need to run the simulation script. (It could be fun to read through it and see how it works, though!)

First download the script:

```
wget https://raw.githubusercontent.com/jsarchibald/cs50/2020/fall/exercises/distro/cabbages/simulate.py
```

Then just run:

```
python simulate.py
```

And just like that, we have a bunch of cabbage sales (and a few new customers). Now we can do something with that data.


### 5b. Switch to a SQL file for the rest of this.

We're going to be writing some longer SQL statements for the rest of this exercise, so best to go ahead and create some SQL files so you can edit them and change them incrementally. (Writing longer code in the SQLite program is possible, just tedious.)

To be able to use `check50`, create a file `ozai.sql` for part 6 and `recall.sql` for part 7. You can do this by running the following in your IDE's terminal:

```
touch ozai.sql recall.sql
```

### 5c. If you run into trouble, reset your database.

If your code behaves unexpectedly, not to worry. The simulation program you just ran in **(5a)** stored a version of your `cabbages.db` before you ran it as well as after. To reset your database, just run one of:

```
python simulate.py -r before
python simulate.py -r after
```

To restore the code from before running the simulator, or after, respectively.


### 6. The world can't know Ozai likes cabbage.

The Fire Lord loves cabbage, but he doesn't want there to be any traces of his latest purchases from the cabbage merchant. We have a couple tasks here:

1. Update any invoices involving the Fire Lord to point to another customer, so any audits won't look suspicious.
2. Delete Ozai's entry (row) in the customers table.

#### A serious note

If you're ever in a position where you are actually asked to do something like this, you should obviously think about the ethical implications of such an action, and possibly refuse to do it! This is a fictional cover-up using fictional characters to get practice with specific syntax (`UPDATE` and `DELETE`) in SQL. It is **not** an endorsement of such behavior in real life, because accountability and transparency are crucial to the proper functioning of our society.

#### Updating the invoices

Ozai thinks the simplest solution to the transaction records is to just transfer them to his brother Iroh's account. (For simplicity, only Uncle Iroh, not the general from *Korra*, is in the database, so you can query using first names.)

It may be simplest in this case to use a *nested* SQL query to do this. In other words, we can break this problem into smaller steps and then combine those parts to come up with a full solution. For example, we know from reading the [W3Schools reference for UPDATE](https://www.w3schools.com/sql/sql_update.asp) that the syntax for updating row(s) looks something like this:

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition; 
```

This tells SQL to look at the table called `table_name`, specifically at the rows where `condition` is true (for example, a column is equal to a specific value), and for those rows change `column1` to now have the value `value1`, `column2` to have value `value2`, and so on. How can we translate the task to syntax? Let's start by making some pseudocode from the task itself.

**The task**

Update any invoices involving the Fire Lord to have Uncle Iroh listed as the customer instead.

**The pseudocode**

```sql
UPDATE invoices SET customer_id = (customer ID of Iroh) WHERE customer_id = (customer ID of Ozai);
```

So we want to change any invoice attributed to Ozai to instead be attributed to Iroh, basically.

Now that we've broken this problem down like this, we know what we need to do to finish the problem -- we need to find Iroh's customer ID and Ozai's customer ID. Go ahead and use two `SELECT` statements (W3Schools reference [here](https://www.w3schools.com/sql/sql_select.asp)) to find those customer IDs.

Once you've done that, you can nest those two `SELECT` queries into an `UPDATE` query, something like this:

```sql
UPDATE invoices SET customer_id = (SELECT ...) WHERE customer_id = (SELECT ...);
```

The parentheses help SQL understand the order things should be done and prevent the SQL from being malformed.

#### Test your SQL statement

First, make sure your code is inside `ozai.sql`. Then, in your terminal, run the following command:

```
sqlite3 cabbages.db < ozai.sql
```

Any syntax bugs with your script will be reported back to you. You can double-check that there are now no invoices attributed to Ozai by adding to `ozai.sql` a line like this:

```sql
SELECT id FROM invoices WHERE id = (SELECT id FROM customers WHERE name = "Ozai");
```

When you run the `sqlite3 cabbages.db < ozai.sql` command again, you should hopefully see no rows printed out!


#### Deleting Ozai's entry

This last part is relatively simpler compared to the previous one. We're just using the `DELETE` syntax (W3Schools reference [here](https://www.w3schools.com/sql/sql_delete.asp)) to delete Ozai's row in the `customers` table. We know from W3Schools that the general syntax for this looks something like:

```sql
DELETE FROM table_name WHERE condition; 
```

In other words, delete any rows in `table_name` where `condition` is true.

This can be pretty simple -- there's only one person named `Ozai` in the customers table, so we can just delete any row in customers where the name on record is `Ozai`. Write that line, add it to the end of your `ozai.sql`, and we can run a test.

#### Testing your code for deletion

First, make sure your code is inside `ozai.sql`. Then, in your terminal, run the following command:

```
sqlite3 cabbages.db < ozai.sql
```

Any syntax bugs with your script will be reported back to you. You can double-check that Ozai was deleted from `customers` by adding to `ozai.sql` a line like this:

```sql
SELECT id FROM customers WHERE name = "Ozai";
```

When you run `sqlite3 cabbages.db < ozai.sql` again, hopefully you won't see any rows show up on your terminal listing `Ozai` as a customer!

#### check50

I made a check50 for this part of our work with the cabbage merchant!

Run this command in your terminal to check your answers:

```
check50 jsarchibald/cs50/2020/fall/exercises/7/ozai
```


### 7. Recall.

Use `recall.sql` to write your answers for this part.

As we saw in the contextualizing video clip at the beginning of this page, the cabbage merchant sometimes has shoddy quality control. This, unfortunately, is one of those times. Cabbage number **433** has been found to be defective, and we have to recall the entire batch. Ultimately, we want to know how many cabbages were affected, their average (and total) value, and get the emails of the customers we should contact about the problem.


#### How many cabbages were affected?

The cabbage merchant wants a summary stat about the recall: how many cabbages are we looking at? We know that every cabbage in the same batch as cabbage number **433** is included in this number. So we can use a `SELECT` statement with the `COUNT` function to figure out how many cabbages we're dealing with here.

We know from the [W3Schools reference](https://www.w3schools.com/sql/sql_count_avg_sum.asp) that we can get the number of rows from a `SELECT` statement using code like the following:

```sql
SELECT COUNT(column_name)
FROM table_name
WHERE condition; 
```

We can make the `condition` include a nested statement to get the `batch_id` of cabbage number 433. So in pseudocode, we can get the count of cabbage IDs (the count of cabbages) with the same `batch_id` as cabbage number 433 like this:

```sql
SELECT COUNT(id)
FROM cabbages
WHERE batch_id = (batch ID of cabbage # 433); 
```

You should be able to finish this statement with the information provided. Write your answer in `recall.sql`


#### What's the average and total value of the affected cabbages?

These modifications should look very similar to your answer to the previous question, but instead use the `AVG` and `SUM` functions to deal with the `value` column of the `cabbages` table. Append your solutions to `recall.sql`.


#### Who do we need to notify?

The cabbage merchant would like a list, ordered alphabetically by name, of the names and emails of everyone he has to contact about the cabbage recall. You can do this using only nested `SELECT` statements, or you can use a `JOIN` statement (W3Schools reference [here](https://www.w3schools.com/sql/sql_join_inner.asp)) if that makes sense to you.

To break this down, we'll first want to get the `invoice_id` of every cabbage in the batch that was sold. That will tell us which invoice each cabbage belongs to.

Then, we'll want to get the set of distinct `customer_id`s associated with each invoice that may have a bad cabbage. The W3Schools documentation on [`SELECT DISTINCT`](https://www.w3schools.com/sql/sql_distinct.asp) may be useful to that end.

Finally, we'll want to get the `name` and `email` of each customer who has a customer ID in that set, and order those rows alphabetically by name. The W3Schools reference for [`ORDER BY`](https://www.w3schools.com/sql/sql_orderby.asp) will be helpful for that last part.


#### Testing

Everything in `recall.sql` should ultimately take the form of a `SELECT` statement. Expected answers are as follows:

- 300 cabbages affected.
- Average cabbage value: around $3.
- Total cabbage value: around $900.
- Customers to notify: 6 - Aang, Iroh, Katara, Vaatu, Wan Shi Tong, Zuko.


#### check50

I made a check50 for this part of our work with the cabbage merchant!

Run this command in your terminal to check your answers:

```
check50 jsarchibald/cs50/2020/fall/exercises/7/recall
```
