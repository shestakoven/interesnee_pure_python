import requests
from bs4 import BeautifulSoup


def get_links_from(http_address: str) -> list:
    """Get all links from http address"""
    response = requests.get(http_address)

    if not response.ok:
        raise ConnectionError('Website data couldn’t be reached.')

    html_doc = BeautifulSoup(response.text, features='html.parser')
    list_of_a = html_doc.find_all('a')
    list_of_links = list()
    for link in list_of_a:
        list_of_links.append(link.get('href'))
    return list_of_links
