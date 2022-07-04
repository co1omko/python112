from flask import Flask, render_template, url_for

app = Flask(__name__)

menu = [
    {"name": "Гланая", 'url': 'index'},
    {"name": "О компании", 'url': 'about'},
    {"name": "Обратная связь", 'url': 'contact'}
]


@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html", title="Главная", menu=menu)


@app.route("/about")
def about():
    return render_template('about.html', title='Описание', menu=menu)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    return render_template("contact.html", title='Обратная связь', menu=menu)


@app.route("/profile/<path:username>")
def profile(username):
    return f"Пользователь: {username}"


if __name__ == '__main__':
    app.run(debug=True)
