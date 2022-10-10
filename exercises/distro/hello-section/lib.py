from urllib import parse as url
import os
import requests


# The URL Of the submission site
BASE_URL = "https://j50.herokuapp.com"


def get_workspace_id():
    """Returns workspace IDs associated with this codespace instance as a string."""

    try:
        return " ".join(os.listdir("/workspaces"))
    except:
        return None


def submit(data):
    """Submits some data to the server.
    
    Args:
        data (dict): a dictionary of data, mapping keys to values.

    Returns:
        An integer status code from the completed request.
    """

    print("Ok, contacting server...")

    
    data["_CS50_WORKSPACE_ID"] = get_workspace_id()
    r = requests.post(url.urljoin(BASE_URL, "/submit"), data=data)
    
    return r.status_code


def delete(data):
    """Deletes a submission from the server.
    
    Args:
        data (dict): a dictionary of data, mapping keys to values.

    Returns:
        An integer status code from the completed request.
    """
    
    print("Ok, contacting server...")

    data["_CS50_WORKSPACE_ID"] = get_workspace_id()
    r = requests.post(url.urljoin(BASE_URL, "/delete"), data=data)
    
    return r.status_code