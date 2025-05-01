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

def combine_data(g_results, o_results):
    combined = []

    if g_results:
        for item in g_results.get('items', []):
            combined.append({'source': 'Google Books',
                'title': item['volumeInfo'].get('title', 'N/A'),
                'author': item['volumeInfo'].get('authors', ['N/A'])[0],
                'link': item['volumeInfo'].get('infoLink', 'N/A')})
    
    if o_results:
        for doc in o_results.get('docs', []):
            combined.append({
                'source': 'Open Library',
                'title': doc.get('title', 'N/A'),
                'author': doc.get('author_name', ['N/A'])[0],
                'link': f"https://openlibrary.org{doc.get('key', '')}" if 'key' in doc else 'N/A'
            })
    return combined

def main() :
    print("Welcome to the Book aggregator!")
    book = input("Enter a book title: ")
    g_results = search_google_books(book)
    o_results = search_open_library(book)

    combined_data = combine_data(g_results, o_results)
    display_results(combined_data)

if __name__ == "__main__":
    main()