from flask import Flask, render_template

app = Flask(__name__)  # Створюємо веб–додаток Flask

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


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True  # автоматичне оновлення шаблонів
    app.run(debug=True)  # Запускаємо веб-сервер з цього файлу в режимі налагодження