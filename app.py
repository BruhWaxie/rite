from flask import Flask, render_template, request, jsonify
from db_scripts import DBManager
from dotenv import load_dotenv
load_dotenv()
import os
import html

app = Flask(__name__)  # Створюємо веб–додаток Flask
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
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
    categories = db.get_categories()
    articles = db.get_articles()
    return render_template("explore.html", categories=categories, articles=articles)

@app.route("/article/<int:article_id>")  # Вказуємо url-адресу для виклику функції
def article_page(article_id):
    article = db.get_article(article_id)
    text = html.unescape(article[3])
    return render_template("article.html", article=article, text=text, title=article[1], description=article[5])

@app.route("/account")  # Вказуємо url-адресу для виклику функції
def account():
    return render_template("account-info.html")

@app.route("/create-article", methods=['GET', 'POST'])  # Вказуємо url-адресу для виклику функції
def create():
    categories = db.get_categories()
    if request.method == 'POST':
        data = request.get_json()
        title = data.get('title')
        content = html.escape(data.get('content'))
        category = data.get('category')
        description = data.get('description')
        db.create_article(title, description, content, 1, category)

        message = {'success':True,'massage':'Successully created article'}
        return jsonify(message)
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

@app.route("/search")  # Вказуємо url-адресу для виклику функції
def search_page():
    query = request.args.get('query', '')
    categories = db.get_categories()
    articles = db.search_articles(query)
    return render_template("search-page.html",categories=categories, articles=articles, category_name=query)

@app.route("/category/<int:category_id>")  # Вказуємо url-адресу для виклику функції
def category_page(category_id):
    categories = db.get_categories()
    articles = db.get_articles_by_category(category_id)
    return render_template("search-page.html", categories=categories, articles=articles, category_name=categories[category_id][1])


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True  # автоматичне оновлення шаблонів
    app.run(debug=True)  # Запускаємо веб-сервер з цього файлу в режимі налагодження