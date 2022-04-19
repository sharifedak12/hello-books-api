from flask import Blueprint, jsonify

class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

books = [
    Book(1, "Python Crash Course", "A hands-on, project based introduction to programming."),
    Book(2, "Cracking the Coding Interview", "189 programming questions and solutions."),
    Book(3, "The Elephant Vanishes", "A collection of short stories by Haruki Marakami.")]

books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods=["GET"])
def handle_books():
    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })
    return jsonify(books_response)
