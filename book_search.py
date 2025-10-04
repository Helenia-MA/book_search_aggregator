import requests
from functools import lru_cache

@lru_cache(maxsize = 128)
def cached_google_books_search(title, author = ""):
    query = f"{title}+inauthor:{author}" if author else title
    url = f"https://www.googleapis.com/books/v1/volumes?q={title, author}"
    response = requests.get(url)
    return response.json()

@lru_cache(maxsize = 128)
def cached_open_library_search(title, author=""):
    url = f"https://openlibrary.org/search.json?title={title}"
    if author:
        url += f"&author={author}"
    response = requests.get(url)
    return response.json()

def search_google_books(title, author = ""):
    return cached_google_books_search(title, author)

def search_open_library(title, author = ""):
    return cached_open_library_search(title, author)

def combine_data(g_results, o_results):
    combined = []

    if g_results:
        for item in g_results.get('items', []):
            volume = item.get('volumeinfo', {})
            image = volume.get('imageLinks', {}).get('thumbnail', None)                  
            combined.append({'source': 'Google Books',
                'title': volume.get('title', 'N/A'),
                'author': ivolume.get('authors', ['N/A'])[0],
                'link': volume.get('infoLink', 'N/A'),
                'image': image
             })
    
    if o_results:
        for doc in o_results.get('docs', []):
            combined.append({
                'source': 'Open Library',
                'title': doc.get('title', 'N/A'),
                'author': doc.get('author_name', ['N/A'])[0],
                'link': f"https://openlibrary.org{doc.get('key', '')}" if 'key' in doc else 'N/A',
                'image': image 
            })
    return combined




