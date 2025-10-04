from flask import Flask, render_template, request
from book_search import search_google_books, search_open_library, combine_data

app= Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def home():
  results = []
  if request.method ="POST":
        book = request.form.get("title")
        author = request.form.get("author")
        g_results = search_google_books(book, author)
        o_results = search_open_library(book, author)
        results = combine_data(g_results, o_results)
    return render_template("index.html", results=results)

if __name__ = "__main__":
    app.run(debug=True)

