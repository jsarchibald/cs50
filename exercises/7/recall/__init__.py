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

    db = SQL("sqlite:///cabbages.db")
    num = db.execute("SELECT COUNT(id) FROM cabbages WHERE batch_id=33")

    if num["COUNT(id)"] not in res:
        raise check50.Failure("COUNT query fails to count cabbages affected")


@check50.check(exists)
def average_works():
    """AVG query averages value of the affected cabbages"""

    res = check50.run("sqlite3 cabbages.db < recall.sql").stdout()

    db = SQL("sqlite:///cabbages.db")
    num = db.execute("SELECT AVG(value) FROM cabbages WHERE batch_id=33")

    if num["AVG(value)"] not in res:
        raise check50.Failure("AVG query fails to find average value of cabbages affected")


@check50.check(exists)
def sum_works():
    """SUM query gets total value of the affected cabbages"""

    res = check50.run("sqlite3 cabbages.db < recall.sql").stdout()

    db = SQL("sqlite:///cabbages.db")
    num = db.execute("SELECT SUM(value) FROM cabbages WHERE batch_id=33")

    if num["SUM(value)"] not in res:
        raise check50.Failure("SUM query fails to find total value of cabbages affected")


@check50.check(exists)
def sum_works():
    """SUM query gets total value of the affected cabbages"""

    res = check50.run("sqlite3 cabbages.db < recall.sql").stdout()

    db = SQL("sqlite:///cabbages.db")
    customers = db.execute("SELECT name, email FROM customers WHERE id IN (SELECT customer_id FROM invoices WHERE id IN (SELECT invoice_id FROM cabbages WHERE batch_id=33)) ORDER BY name")

    val = ".*".join([f"{row['name']} | {row['email']}" for row in customers])

    if re.match(f".*{val}.*", res) is None:
        raise check50.Failure("SUM query fails to find total value of cabbages affected")
