from datetime import datetime, timedelta

from data import DEFAULT_STATUS


def insert_flight(db, form):
    """Inserts a flight into the database."""
    timestamp = f"{form['date']} {form['hour']}:{form['minute']}"

    ts = datetime.strptime(timestamp, "%Y-%m-%d %H:%M")
    unix_ts = ts.timestamp()

    db.execute("INSERT INTO flights (origin, destination, status, departure) VALUES (?, ?, ?, ?);",
               form["origin"],
               form["destination"],
               DEFAULT_STATUS,
               unix_ts)


def to_timestamp(t):
    """Prettifies a UNIX timestamp to be human-readable."""

    dt = datetime.fromtimestamp(t)
    tomorrow = datetime.today() + timedelta(days=1)

    if dt >= tomorrow:
        return dt.strftime("%I:%M %p (%a, %b %d)")

    return dt.strftime("%I:%M %p")
