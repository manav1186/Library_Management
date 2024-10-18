from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this in production!

# Sample book data
books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "available": True},
    {"id": 2, "title": "1984", "author": "George Orwell", "available": True},
    {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee", "available": False},
    {"id": 4, "title": "Moby-Dick", "author": "Herman Melville", "available": True},
    {"id": 5, "title": "War and Peace", "author": "Leo Tolstoy", "available": True},
    {"id": 6, "title": "Pride and Prejudice", "author": "Jane Austen", "available": True},
    {"id": 7, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "available": False},
    {"id": 8, "title": "The Hobbit", "author": "J.R.R. Tolkien", "available": True},
    {"id": 9, "title": "Ulysses", "author": "James Joyce", "available": False},
    {"id": 10, "title": "Brave New World", "author": "Aldous Huxley", "available": True},
]

@app.route('/')
def home():
    search_query = request.args.get('search', '')
    filtered_books = [book for book in books if search_query.lower() in book['title'].lower() or search_query.lower() in book['author'].lower()]
    return render_template('index.html', books=filtered_books, search_query=search_query)

@app.route('/borrow/<int:book_id>')
def borrow_book(book_id):
    for book in books:
        if book['id'] == book_id and book['available']:
            book['available'] = False
            flash(f'You have borrowed "{book["title"]}"', 'success')
            break
    return redirect(url_for('home'))

@app.route('/return/<int:book_id>')
def return_book(book_id):
    for book in books:
        if book['id'] == book_id and not book['available']:
            book['available'] = True
            flash(f'You have returned "{book["title"]}"', 'success')
            break
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)