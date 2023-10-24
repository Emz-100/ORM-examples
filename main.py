# Import the necessary modules
from django.db import models
from django.db.models import Q

# Define a simple model for a Book
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publication_year = models.IntegerField()

# Create a new book record
def create_book():
    book = Book(title="Sample Book", author="John Doe", publication_year=2023)
    book.save()

# Retrieve all books
def get_all_books():
    books = Book.objects.all()
    for book in books:
        print(f"{book.title} by {book.author}, published in {book.publication_year}")

# Update a book record
def update_book(book_id, new_title):
    book = Book.objects.get(pk=book_id)
    book.title = new_title
    book.save()

# Delete a book record
def delete_book(book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()

# Main function to demonstrate ORM operations
if __name__ == "__main__":
    # Create a new book
    create_book()

    # Retrieve all books
    print("All Books:")
    get_all_books()

    # Update a book's title
    book_id_to_update = 1  # Assuming the book's ID is 1
    new_title = "Updated Book Title"
    update_book(book_id_to_update, new_title)

    # Delete a book
    book_id_to_delete = 1  # Assuming the book's ID is 1
    delete_book(book_id_to_delete)

    # Retrieve all books after updates and deletions
    print("\nAll Books (after update and delete operations):")
    get_all_books()
