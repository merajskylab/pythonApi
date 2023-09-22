import flask
from flask import Flask, jsonify, request


app = Flask(__name__)

# Sample data (in-memory list)
books = [
  {"id": 1, "book_name": "To Kill a Mockingbird", "author_name": "Harper Lee"},
  {"id": 2, "book_name": "1984", "author_name": "George Orwell"},
  {"id": 3, "book_name": "The Great Gatsby", "author_name": "F. Scott Fitzgerald"},
  {"id": 4, "book_name": "Brave New World", "author_name": "Aldous Huxley"},
  {"id": 5, "book_name": "Pride and Prejudice", "author_name": "Jane Austen"},
  {"id": 6, "book_name": "The Catcher in the Rye", "author_name": "J.D. Salinger"},
  {"id": 7, "book_name": "To the Lighthouse", "author_name": "Virginia Woolf"},
  {"id": 8, "book_name": "Moby-Dick", "author_name": "Herman Melville"},
  {"id": 9, "book_name": "The Lord of the Rings", "author_name": "J.R.R. Tolkien"},
  {"id": 10, "book_name": "The Hobbit", "author_name": "J.R.R. Tolkien"},
  {"id": 11, "book_name": "War and Peace", "author_name": "Leo Tolstoy"},
  {"id": 12, "book_name": "The Odyssey", "author_name": "Homer"},
  {"id": 13, "book_name": "Crime and Punishment", "author_name": "Fyodor Dostoevsky"},
  {"id": 14, "book_name": "Frankenstein", "author_name": "Mary Shelley"},
  {"id": 15, "book_name": "The Grapes of Wrath", "author_name": "John Steinbeck"}
]



# Routes for CRUD operations
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = next((book for book in books if book["id"] == id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404
    

@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.get_json()
    new_book["id"] = len(books) + 1  # Assign a new ID
    books.append(new_book)
    return jsonify({"message": "Book created successfully"})

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = next((book for book in books if book["id"] == id), None)
    if book:
        updated_data = request.get_json()
        book.update(updated_data)
        return jsonify({"message": "Book updated successfully"})
    else:
        return jsonify({"error": "Book not found"}), 404

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = next((book for book in books if book["id"] == id), None)
    if book:
        books.remove(book)
        return jsonify({"message": "Book deleted successfully"})
    else:
        return jsonify({"error": "Book not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
