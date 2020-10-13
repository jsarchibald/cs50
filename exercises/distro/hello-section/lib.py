from urllib import parse as url
import requests


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

    r = requests.post(url.urljoin(BASE_URL, "/delete"), data=data)
    
    return r.status_code
