import os
from flask import Flask, jsonify
from database.books import books

app = Flask(__name__)

@app.route('/<string:isbn>', methods=['GET'])
def search_book(isbn):
    for book in books:
        if book['isbn13'] == isbn or book['isbn10'] == isbn:
            return jsonify(book)

    return jsonify({"error": "Book not found"}), 404

if __name__ == '__main__':
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        print("""
        --------------------------------------------
        Usage:
        - Make a GET request to http://127.0.0.1:5000/ + ISBN
        - Replace 'ISBN' with the actual ISBN number.

        Example:
        - To search for a book with ISBN '0060935464', use:
          http://127.0.0.1:5000/0060935464

        Mock data is located in 'database/books.py'.
        --------------------------------------------
        """)
    app.run(debug=True)
