# Simulates Cabbage Corp. transactions, restores databases as needed

import random
import sys
import zipfile

from cs50 import SQL


def main():
    if len(sys.argv) < 3:
        simulate()

    elif sys.argv[1] == "-r":
        restore(sys.argv[2])


def restore(version):
    try:
        z = zipfile.ZipFile("Cabbages.Backup.zip", "r")
    except:
        print("Couldn't open backup ZIP file.")

    data = None
    if version == "before":
        data = z.read("before.db")
    elif version == "after":
        data = z.read("after.db")

    if data is not None:
        with open("cabbages.db", "wb") as f:
            f.write(data)

    return


def simulate():

    print("starting simulation")

    # Backup before
    with open("cabbages.db", "rb") as f:
        before = f.read()


    db = SQL("sqlite:///cabbages.db")


    # Clear invoices and cabbages
    clear = ["invoices", "cabbages"]
    for table in clear:
        db.execute(f"DELETE FROM {table}")

    print(f"cleared existing data from {', '.join(clear)}")


    # Price per pound of different cabbage types, from https://www.ers.usda.gov/webdocs/DataFiles/51035/cabbage.xlsx?v=9564
    CABBAGE_TYPES = {
        "Green": .62,
        "Red": 1.02,
        "Sauerkraut": 1.15
    }


    # Characters and their emails
    CHARACTERS = {
        "Aang": "aang@team.avatar",
        "Admiral Zhao": "zhao@fire.gov",
        "Azula": "azula@fire.gov",
        "Iroh": "iroh@fire.gov",
        "Katara": "katara@team.avatar",
        "Long Feng": "lf@dai-li.earth.gov",
        "Mai": "mai@fire.gov",
        "Ozai": "ozai@fire.gov",
        "Sokka": "sokka@team.avatar",
        "Suki": "suki@kyoshi.earth.gov",
        "Toph": "toph@team.avatar",
        "Ty Lee": "tylee@fire.gov",
        "Wan Shi Tong": "owl.spirit@fas.harvard.edu",
        "Vaatu": "vaatu@spirit.gov",
        "Zuko": "zuko@fire.gov"
    }


    # Constants about the recall parameters
    RECALL = {
        "known_infected": 433,
        "batch_id": 33,
        "affected": ["Aang", "Katara", "Ozai", "Vaatu", "Wan Shi Tong", "Zuko"]
    }


    # Constants about populating the database
    BATCHES = 40
    CABBAGES = 4000
    INVOICES = 400


    # Insert remaining customers into table
    chars = set(CHARACTERS.keys())
    created = set([row["name"] for row in db.execute("SELECT name FROM customers;")])
    to_create = chars.difference(created)

    for c in to_create:
        db.execute("INSERT INTO customers (name, email) VALUES (?, ?);", c, CHARACTERS[c])

    print("created customers")

    # Get customer IDs and names
    name_to_id = {c["name"]: c["id"] for c in db.execute("SELECT id, name FROM customers;")}
    id_to_name = {c["id"]: c["name"] for c in db.execute("SELECT id, name FROM customers;")}


    # Create invoices
    invoice_query = "INSERT INTO invoices (customer_id, total_value) VALUES"
    cabbage_query = "INSERT INTO cabbages (cabbage_type, batch_id, invoice_id, value) VALUES"

    for invoice in range(INVOICES):
        customer_id = name_to_id[random.choice(list(CHARACTERS.keys()))]
        total_value = 0
        for c in range(CABBAGES // INVOICES):

            # Assign cabbage a random type, and then value based on price per pound (using normal distribution)
            cabbage_type = random.choice(list(CABBAGE_TYPES.keys()))
            value = round(CABBAGE_TYPES[cabbage_type] * random.normalvariate(2, .4), 2)  # 2lb from the internet, sdev made up
            total_value += value

            # Assign cabbage a random batch number
            batch_id = random.randint(1, BATCHES)

            # Hard-code a specific cabbage to go bad for purposes of specification
            if c + invoice * (CABBAGES // INVOICES) == RECALL["known_infected"] - 1:
                batch_id = RECALL["batch_id"]

            if batch_id == RECALL["batch_id"]:
                customer_id = name_to_id[random.choice(RECALL["affected"])]

            # I am generating the values, so I can trust them. There is no user input here. So format strings are ok-ish.
            cabbage_query += f" ('{cabbage_type}', {batch_id}, {invoice + 1}, {value}),"

        invoice_query += f" ({customer_id}, {total_value}),"


    # Insert invoices
    db.execute(invoice_query[:-1] + ";")
    print("created invoices")


    # Insert cabbages
    db.execute(cabbage_query[:-1] + ";")
    print("created cabbages")


    # Backup after
    with open("cabbages.db", "rb") as f:
        after = f.read()


    # Write backups to ZIP file
    z = zipfile.ZipFile("Cabbages.Backup.zip", "w")
    z.writestr("before.db", before)
    z.writestr("after.db", after)
    z.close()


    print("backed up database before and after")


if __name__ == "__main__":
    main()
