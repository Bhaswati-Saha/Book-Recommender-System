from flask import Flask, render_template, request
import recommendation

app = Flask(__name__)



@app.route('/')
def index():
    return render_template("index.html")


@app.route('/recommend', methods=['post'])
def predict():
    book_name = request.form.get('title')
    if book_name not in recommendation.book_pivot.index:
        response = ['Book not found']
    else:
        response = recommendation.recommend_book(book_name)

    return render_template("index.html", response=response)


if __name__ == "__main__":
    app.run(debug=True)