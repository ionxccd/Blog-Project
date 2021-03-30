from flask import Flask, request, render_template
import sqlite3
from datetime import datetime
import time
import os.path

app = Flask(__name__, template_folder = "blog_folder")

conn = sqlite3.connect("blog_info.db")
cursor = conn.cursor()
now = datetime.now()
#cursor.execute("CREATE TABLE blog_infos(title, author, date, content)")
#cursor.execute("""INSERT INTO blog_infos(
#        title, author, date, content) VALUES("Seomthing", "David", "123", "SomethingSomething")"""
@app.route("/")
def index():
    conn = sqlite3.connect("blog_info.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM blog_infos ORDER BY rowid DESC")
    all_datat = cursor.fetchall()
    conn.commit()
    conn.close()
    return render_template("blog_home.html", blog_info = all_datat)

@app.route("/link")
def links():
    return render_template("admin_page.html")

@app.route("/login_user/", methods = ["POST"])
def enter():
    username = request.form['username']
    passsw = request.form['password']
    return render_template("")

@app.route("/create_post/", methods = ["POST"])
def post():
    conn = sqlite3.connect("blog_info.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM blog_infos ORDER BY rowid DESC")
    all_datat = cursor.fetchall()
    blog_title = request.form['title']
    blog_content = request.form['content']
    current_date = date_time = time.strftime("%H:%M %p %h %d %Y")
    author = "David"

    tab = """INSERT INTO blog_infos(
        title, author, date, content) VALUES(?, ?, ?, ?);
        """

    values = (blog_title, author, current_date, blog_content)
    cursor.execute(tab, values)
    conn.commit()
    conn.close()
    return render_template("blog_home.html", blog_info = all_datat, flash_message = "True")

conn.commit()
conn.close()
if __name__ == "__main__":
    app.run(debug = True)
