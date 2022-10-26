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

    check50.include("update_works.sql")

    res = check50.run("sqlite3 cabbages.db < ozai.sql").stdout()
    res2 = check50.run("sqlite3 cabbages.db < update_works.sql").stdout()
    
    if res2 != "":
        raise check50.Mismatch("", res2)


@check50.check(update_works)
def delete_works():
    """DELETE query erases Ozai from customers table"""
    
    check50.include("delete_works.sql")
    
    res = check50.run("sqlite3 cabbages.db < delete_works.sql").stdout()
    
    if res != "":
        raise check50.Mismatch("", res)
