import sqlite3
import os
from flask import Flask, render_template, url_for, request, flash, session, redirect, abort, g
from FDateBase import FDateBase

DATABASE = '/tmp/flskHW.db'
DEBUG = True
SECRET_KEY = '79a8ca20ddd5c872c9265f97688af75f00bab4bb'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flskHW.db')))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sql_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route("/index")
@app.route("/")
def index():
    db = get_db()
    dbase = FDateBase(db)
    return render_template("index.html", title="Главная", menu=dbase.get_menu(), kurs=dbase.get_kurs_annonce())


@app.route("/about")
def about():
    print(url_for('about'))
    return render_template('about.html', title='Описание', menu=[])


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash("Сообщение отправлено успешно!", category='success')
        else:
            flash("Ошибка отправки данных", category='error')
    return render_template("contact.html", title='Обратная связь', menu=[])


@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'userLogged' == session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == 'demid' and request.form['passw'] == 123456:
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))

    return render_template('login.html', title="Авторизация", menu=[])


@app.route("/profile/<username>")
def profile(username):
    if 'userLogget' not in session or session['userLogget'] != username:
        abort(401)
    return f"Пользователь: {username}"


@app.route("/add_kurs", methods=["POST", "GET"])
def add_kurs():
    db = get_db()
    dbase = FDateBase(db)

    if request.method == "POST":
        if len(request.form['name']) > 4 and len(request.form['kurs']) > 20 and len(request.form['price']) > 2:
            res = dbase.add_kurs(request.form['name'], request.form['price'], request.form['kurs'])
            if not res:
                flash("Ошибка добаления курса", category='error')
            else:
                flash("Курс добавлен успешно", category='success')
        else:
            flash("Ошибка добаления курса", category='error')
    return render_template("add_kurs.html", title="Добавление курса", menu=dbase.get_menu())


@app.route('/kurs/<int:id_kurs>')
def show_kurs(id_kurs):
    db = get_db()
    dbase = FDateBase(db)
    title, price, kurs = dbase.get_kurs(id_kurs)
    if not title:
        abort(404)
    return render_template('kurs.html', memu=dbase.get_menu(), title=title, price=price, kurs=kurs)


if __name__ == '__main__':
    app.run(debug=True)
