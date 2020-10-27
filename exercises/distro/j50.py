from bs4 import BeautifulSoup
from urllib import parse as url

import requests
import sys


# The URL Of the submission site
BASE_URL = "https://j50.herokuapp.com"


def submit(data):
    """Submits some data to the server.

    Args:
        data (dict): a dictionary of data, mapping keys to values.

    Returns:
        An integer status code from the completed request.
    """

    print("Ok, contacting server...")

    r = requests.post(url.urljoin(BASE_URL, "/html/submit"), data=data)
    print(r.url)

    return r.status_code


def delete(data):
    """Deletes a submission from the server.

    Args:
        data (dict): a dictionary of data, mapping keys to values.

    Returns:
        An integer status code from the completed request.
    """

    print("Ok, contacting server...")

    r = requests.post(url.urljoin(BASE_URL, "/html/delete"), data=data)

    return r.status_code


def main():
    if len(sys.argv) != 3:
        print("Usage: python j50.py <upload/delete> <path-to-html-file/submission-id>")
        sys.exit(1)

    if sys.argv[1] == "upload":
        data = dict()
        with open(sys.argv[2]) as f:
            soup = BeautifulSoup(f, "html.parser")
            data["title"] = soup.title.string

            print(data["title"])
            title = input("Press enter if this title is correct; otherwise, type a new one before pressing enter.\n>> ")
            if title != "":
                data["title"] = title

            f.seek(0)
            data["html"] = f.read()

        if submit(data) == 200:
            print(f"Successfully uploaded {sys.argv[2]}.")
        else:
            print(f"Error uploading {sys.argv[2]}.")

    elif sys.argv[1] == "delete":
        if delete({"id": sys.argv[2]}) == 200:
            print(f"Successfully deleted submission #{sys.argv[2]}")
        else:
            print(f"Error deleting submission #{sys.argv[2]}")


if __name__ == "__main__":
    main()
