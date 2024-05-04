from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
    {"id": 3, "title": "Book 3", "author": "Author 3"}
]

@app.route('/')
def index():
    return render_template('index.html', books=books)

@app.route('/book/<int:book_id>')
def book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return render_template('book.html', book=book)
    return 'Book not found', 404

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        book_id = len(books) + 1
        new_book = {"id": book_id, "title": title, "author": author}
        books.append(new_book)
        return redirect(url_for('index'))
    return render_template('add_book.html')

if __name__ == '__main__':
    app.run(debug=True)