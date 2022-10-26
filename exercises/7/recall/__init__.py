from calendar import c
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

    check50.include("count_works.sql")

    res = check50.run("sqlite3 cabbages.db < recall.sql").stdout()
    expected = check50.run('sqlite3 cabbages.db < count_works.sql').stdout()

    if expected not in res:
        raise check50.Mismatch(expected, res)


@check50.check(exists)
def average_works():
    """AVG query averages value of the affected cabbages"""
    
    check50.include("average_works.sql")

    res = check50.run("sqlite3 cabbages.db < recall.sql").stdout()
    expected = check50.run('sqlite3 cabbages.db < average_works.sql').stdout()

    if expected not in res:
        raise check50.Mismatch(expected, res)


@check50.check(exists)
def sum_works():
    """SUM query gets total value of the affected cabbages"""

    check50.include("sum_works.sql")

    res = check50.run("sqlite3 cabbages.db < recall.sql").stdout()
    expected = check50.run('sqlite3 cabbages.db < sum_works.sql').stdout()

    if expected not in res:
        raise check50.Mismatch(expected, res)


@check50.check(exists)
def names():
    """gets names and emails of affected customers"""

    check50.include("names.sql")

    res = check50.run("sqlite3 cabbages.db < recall.sql").stdout()
    expected = check50.run('sqlite3 cabbages.db < names.sql').stdout()

    if expected not in res:
        raise check50.Mismatch(expected, res)
