import requests
from tabulate import tabulate 
def search_google_books(title):
    url = f"https://www.googleapis.com/books/v1/volumes?q={title}"
    response = requests.get(url)
    return response.json()

def search_open_library(title):
    url = f"https://openlibrary.org/search.json?title={title}"
    response = requests.get(url)
    return response.json()

def display_results(results):
    headers = ["Source", "Title", "Author", "Link"]
    table = [[r['source'], r['title'], r['author'], r['link']] for r in results]
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))