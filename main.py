from tabulate import tabulate
#from prettytable import PrettyTable
from book_search import search_google_books, search_open_library, combine_data

def display_results(results):
    headers = ["Source", "Title", "Author", "Link"]
    table = [[r['source'], r['title'], r['author'], r['link']] for r in results]
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
    #table = PrettyTable()
    #table.field_names = ["Source", "Title", "Author", "Link"]

    #for result in results:
    #    table.add_row([result["source"], result["title"], result["author"], result["link"]])

    #print(table)
    
def main() :
    print("Welcome to the Book aggregator!")
    book = input("Enter a book title: ")
    author = input("Enter author's name (or leave blank to skip): ")
    g_results = search_google_books(book, author)
    o_results = search_open_library(book, author)

    combined_data = combine_data(g_results, o_results)
    display_results(combined_data)

if __name__ == "__main__":
    main()
