import check50

from cs50 import SQL


@check50.check()
def exists():
    """ozai.sql exists"""
    check50.exists("ozai.sql")
    check50.include("cabbages.db")


@check50.check(exists)
def update():
    """ozai.sql contains UPDATE query"""

    log = open("ozai.sql").read().lower()
    if "update" not in log:
        raise check50.Failure(f"missing UPDATE query in ozai.sql")


@check50.check(exists)
def delete():
    """ozai.sql contains DELETE query"""

    log = open("ozai.sql").read().lower()
    if "delete" not in log:
        raise check50.Failure(f"missing DELETE query in ozai.sql")


@check50.check(exists)
def update_works():
    """UPDATE query erases all references to Ozai"""

    db = SQL("sqlite:///cabbages.db")
    ozai_id = db.execute("SELECT id FROM customers WHERE name=?", "Ozai")

    db._close_session()

    check50.run("sqlite3 cabbages.db < ozai.sql")

    res = check50.run('sqlite3 cabbages.db "SELECT id FROM invoices WHERE customer_id={}"'.format(ozai_id)).stdout()
    res2 = check50.run('sqlite3 cabbages.db "SELECT id FROM invoices WHERE customer_id={}"'.format(ozai_id)).stdout()
    raise check50.Mismatch(res, res2)

    #n = db.execute("SELECT COUNT(id) FROM invoices WHERE customer_id=?", ozai_id[0]["id"])

    #if n[0]["COUNT(id)"] > 0:
    #    raise check50.Mismatch("UPDATE query fails to erase all references to Ozai in invoices", n)


@check50.check(update_works)
def delete_works():
    """DELETE query erases Ozai from customers table"""
    
    db = SQL("sqlite:///cabbages.db")
    n = db.execute("SELECT COUNT(id) FROM customers WHERE name=?", "Ozai")
    if n[0]["COUNT(id)"] > 0:
        raise check50.Failure("DELETE query fails to erase Ozai from customers table")
 
