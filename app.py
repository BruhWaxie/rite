from flask import Flask, render_template, request
from db_scripts import DBManager


app = Flask(__name__)  # Створюємо веб–додаток Flask

db = DBManager('rite.db')

@app.route("/")  # Вказуємо url-адресу для виклику функції
def index():
    return render_template("index.html") 

@app.route("/login")  # Вказуємо url-адресу для виклику функції
def login():
    return render_template("login.html") 

@app.route("/register")  # Вказуємо url-адресу для виклику функції
def register():
    return render_template("register.html")

@app.route("/explore")  # Вказуємо url-адресу для виклику функції
def explore():
    return render_template("explore.html")

@app.route("/article")  # Вказуємо url-адресу для виклику функції
def article():
    return render_template("article.html")

@app.route("/account")  # Вказуємо url-адресу для виклику функції
def account():
    return render_template("account-info.html")

@app.route("/create-article")  # Вказуємо url-адресу для виклику функції
def create():
    categories = db.get_categories()
    return render_template("create.html", categories=categories, category_name=categories[1])

@app.route("/ua")  # Вказуємо url-адресу для виклику функції
def index_ua():
    return render_template("index-ua.html")

@app.route("/ua/login")  # Вказуємо url-адресу для виклику функції
def login_ua():
    return render_template("login-ua.html")

@app.route("/ua/register")  # Вказуємо url-адресу для виклику функції
def register_ua():
    return render_template("register-ua.html")

@app.route("/ua/article")  # Вказуємо url-адресу для виклику функції
def article_ua():
    return render_template("article-ua.html")

@app.route("/ua/create-article")  # Вказуємо url-адресу для виклику функції
def create_ua():
    return render_template("create-ua.html")


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True  # автоматичне оновлення шаблонів
    app.run(debug=True)  # Запускаємо веб-сервер з цього файлу в режимі налагодження