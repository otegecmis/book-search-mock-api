## Book Search Mock API

A simple mock API that provides search functionality for books by ISBN.

### Installation

Ensure you have `Python 3.x`, the `pip` package manager, and `virtualenv` installed on your system.

#### Steps

1. **Clone the repository**

```sh
git clone https://github.com/otegecmis/book-search-mock-api.git
```

2. **Navigate to the project directory**

```sh
cd book-search-mock-api
```

3. **Create and activate a virtual environment**

```sh
virtualenv env
. env/bin/activate
```

4. **Install dependencies**

```sh
pip3 install -r requirements.txt
```

5. **Run the application**

```sh
python3 app.py
```

### Usage

Once the server is running, you can search for a book by its ISBN by making a GET request to:

```text
http://127.0.0.1:5000/books/search/ + ISBN
```

Replace `ISBN` with the actual ISBN number you want to search for.

For example, to search for a book with ISBN `0060935464`, use:

```text
http://127.0.0.1:5000/books/search/0060935464
```
