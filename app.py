import os
import re
from flask import Flask, jsonify
from flask_cors import CORS
from database.books import books

app = Flask(__name__)
CORS(app)

def validate_isbn(isbn):
    isbn10_pattern = r'^\d{9}[\dX]$'
    isbn13_pattern = r'^\d{13}$'

    return bool(re.match(isbn10_pattern, isbn) or re.match(isbn13_pattern, isbn))

@app.route('/<string:isbn>', methods=['GET'])
def search_book(isbn):
    if not validate_isbn(isbn):
        return jsonify({
            "error": "Invalid ISBN Format",
            "message": "Please provide a valid ISBN-10 or ISBN-13."
        }), 400
    
    for book in books:
        if book['isbn13'] == isbn or book['isbn10'] == isbn:
            return jsonify(book)

    return jsonify({
        "error": "Not Found",
        "message": f"No book found with ISBN: {isbn}."
    }), 404

@app.errorhandler(Exception)
def handle_error(error):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(error)
    }), 500

if __name__ == '__main__':
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        print("""
        --------------------------------------------
        Book Search Mock API
        
        Endpoint:
        GET /<isbn>
        
        Examples:
        - ISBN-13: http://127.0.0.1:5000/9780747532699
        - ISBN-10: http://127.0.0.1:5000/0747532699
        
        Response Codes:
        - 200: Success
        - 400: Invalid ISBN Format
        - 404: Not Found
        - 500: Server Error
        
        Mock data is located in 'database/books.py'.
        --------------------------------------------
        """)
    app.run(debug=True)
