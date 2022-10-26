import check50

from cs50 import SQL


@check50.check()
def exists():
    """cabbages.db exists"""
    check50.exists("cabbages.db")


@check50.check(exists)
def tables_exist():
    """cabbages.db contains correct tables"""

    res = check50.run('sqlite3 cabbages.db ".table"').stdout()
    expected = "cabbages   customers  invoices \n"

    if "cabbages" not in res or "customers" not in res or "invoices" not in res:
        raise check50.Mismatch(res, expected)


@check50.check(exists)
def cabbages_table():
    """cabbages table contains correct columns"""

    res = check50.run('sqlite3 cabbages.db ".schema cabbages"').stdout()
    expected = "CREATE TABLE cabbages (\n    id INTEGER PRIMARY KEY,\ncabbage_type TEXT NOT NULL,\nbatch_id INTEGER NOT NULL,\n    invoice_id INTEGER NOT NULL,\n    value REAL NOT NULL\n);\n"

    passing = True
    for item in ["id INTEGER", "PRIMARY KEY", "cabbage_type TEXT NOT NULL", "batch_id INTEGER NOT NULL", "invoice_id INTEGER NOT NULL", "value REAL NOT NULL"]:
        if item not in res:
            passing = False

    if not passing:
        raise check50.Mismatch(expected, res)


@check50.check(exists)
def customers_table():
    """customers table contains correct columns"""

    res = check50.run('sqlite3 cabbages.db ".schema customers"').stdout()
    expected = "CREATE TABLE customers (\n    id INTEGER PRIMARY KEY,\n    name TEXT NOT NULL,\n    email TEXT NOT NULL\n);\n"

    passing = True
    for item in ["id INTEGER", "PRIMARY KEY", "name TEXT NOT NULL", "email TEXT NOT NULL"]:
        if item not in res:
            passing = False

    if not passing:
        raise check50.Mismatch(expected, res)


@check50.check(exists)
def invoices_table():
    """invoices table contains correct columns"""

    res = check50.run('sqlite3 cabbages.db ".schema invoices"').stdout()
    expected = "CREATE TABLE invoices (\n    id INTEGER PRIMARY KEY,\n    customer_id INTEGER NOT NULL,\n    total_value REAL NOT NULL\n);\n"

    passing = True
    for item in ["id INTEGER", "PRIMARY KEY", "customer_id INTEGER NOT NULL", "total_value REAL NOT NULL"]:
        if item not in res:
            passing = False

    if not passing:
        raise check50.Mismatch(expected, res)


@check50.check(customers_table)
def inserted_two_customers():
    """customers table contains at least two rows"""

    res = check50.run('sqlite3 cabbages.db < inserted_two_customers.sql').stdout()
    check50.log(res)
    check50.log(res.count("\n"))

    if res.count("\n") < 2:
        raise check50.Failure("customers table doesn't have at least two rows")
