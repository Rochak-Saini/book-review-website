from flask import Flask, render_template, request, redirect, url_for
import requests
from models import db, Book, Review
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db.init_app(app)

# Create the database
with app.app_context():
    db.create_all()

migrate = Migrate(app, db)

# ... (routes and other code will go here) ...
@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)


@app.route('/add-book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        description = request.form['description']
        genre = request.form['genre']
        publication_year = request.form['publication_year']

        book = Book(title=title, author=author, description=description, genre=genre, publication_year=publication_year)
        db.session.add(book)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add_book.html')

@app.route('/books/<int:book_id>/add-review', methods=['GET', 'POST'])
def add_review(book_id):
    book = Book.query.get_or_404(book_id)
    if request.method == 'POST':
        user_name = request.form['user_name']
        rating = request.form['rating']
        comment = request.form['comment']

        review = Review(book_id=book_id, user_name=user_name, rating=rating, comment=comment)
        db.session.add(review)
        db.session.commit()

        return redirect(url_for('book_details', book_id=book_id))

    return render_template('add_review.html', book=book)

@app.route('/books/<int:book_id>', methods=['GET'])
def book_details(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('book_details.html', book=book)

@app.route('/reviews/<int:review_id>/delete', methods=['POST'])
def delete_review(review_id):
    review = Review.query.get_or_404(review_id)
    book_id = review.book_id
    db.session.delete(review)
    db.session.commit()
    return redirect(url_for('book_details', book_id=book_id))

if __name__ == '__main__':
    app.run(debug=True)
    # Add this line
    with app.app_context():
        db.create_all()
        migrate.init_app(app, db)