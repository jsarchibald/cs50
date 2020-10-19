import check50
import re

from cs50 import SQL


@check50.check()
def exists():
    """recall.sql exists"""
    check50.exists("recall.sql")
    check50.include("cabbages.db")


@check50.check(exists)
def counts():
    """recall.sql contains COUNT query"""

    log = open("recall.sql").read().lower()
    if "count" not in log:
        raise check50.Failure(f"missing COUNT query in recall.sql")


@check50.check(exists)
def averages():
    """recall.sql contains AVG query"""

    log = open("recall.sql").read().lower()
    if "avg" not in log:
        raise check50.Failure(f"missing AVG query in recall.sql")


@check50.check(exists)
def sums():
    """recall.sql contains SUM query"""

    log = open("recall.sql").read().lower()
    if "sum" not in log:
        raise check50.Failure(f"missing SUM query in recall.sql")


@check50.check(exists)
def orders():
    """recall.sql contains ORDER BY"""

    log = open("recall.sql").read().lower()
    if "order by" not in log:
        raise check50.Failure(f"missing ORDER BY in recall.sql")


@check50.check(exists)
def count_works():
    """COUNT query counts the affected cabbages"""

    res = check50.run("sqlite3 cabbages.db < recall.sql").stdout()
    expected = check50.run('sqlite3 cabbages.db "SELECT COUNT(id) FROM cabbages WHERE batch_id=33;"').stdout()

    if expected not in res:
        raise check50.Mismatch(expected, res)


@check50.check(exists)
def average_works():
    """AVG query averages value of the affected cabbages"""

    res = check50.run("sqlite3 cabbages.db < recall.sql").stdout()
    expected = check50.run('sqlite3 cabbages.db "SELECT AVG(value) FROM cabbages WHERE batch_id=33;"').stdout()

    if expected not in res:
        raise check50.Mismatch(expected, res)


@check50.check(exists)
def sum_works():
    """SUM query gets total value of the affected cabbages"""

    res = check50.run("sqlite3 cabbages.db < recall.sql").stdout()
    expected = check50.run('sqlite3 cabbages.db "SELECT SUM(value) FROM cabbages WHERE batch_id=33;"').stdout()

    if expected not in res:
        raise check50.Mismatch(expected, res)


@check50.check(exists)
def names():
    """gets names and emails of affected customers"""

    res = check50.run("sqlite3 cabbages.db < recall.sql").stdout()
    expected = check50.run('sqlite3 cabbages.db "SELECT name, email FROM customers WHERE id IN (SELECT customer_id FROM invoices WHERE id IN (SELECT invoice_id FROM cabbages WHERE batch_id=33)) ORDER BY name;"').stdout()

    if expected not in res:
        raise check50.Mismatch(expected, res)
