import requests
 
def search_google_books(title, author = ""):
    query = f"{title}+inauthor:{author}" if author else title
    url = f"https://www.googleapis.com/books/v1/volumes?q={title, author}"
    response = requests.get(url)
    return response.json()

def search_open_library(title, author=""):
    url = f"https://openlibrary.org/search.json?title={title}"
    if author:
        url += f"&author={author}"
    response = requests.get(url)
    return response.json()

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
