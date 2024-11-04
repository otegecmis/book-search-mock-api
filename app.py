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
    app.run(debug=True)