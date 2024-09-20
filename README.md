## Book Search Mock API

A simple mock API that provides search functionality for books by ISBN.

### Installation

Ensure you have Python 3.x and the `pip` package manager installed on your system.

#### Steps

1. **Clone the repository**

```sh
    git clone https://github.com/otegecmis/book-search-mock-api.git
```

2. **Navigate to the project directory and install dependencies**

```sh
    cd book-search-mock-api
    pip3 install -r requirements.txt
```

3. **Run the application**

```sh
    python3 app.py
```

### Usage

Once the server is running, you can search for a book by its ISBN using the following endpoint:

http://127.0.0.1:5000/books/search/<ISBN>

Replace `<ISBN>` with the actual ISBN number you want to search for.

#### Example

To search for a book with ISBN `0060935464`, make a GET request to:

http://127.0.0.1:5000/books/search/0060935464
