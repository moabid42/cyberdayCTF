from flask import Flask, request, render_template
from sqlite3 import connect
import re
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
app = Flask(__name__)

# Initialize Limiter
limiter = Limiter(
    get_remote_address, 
    app=app,
    default_limits=["10 per minute"]  # Limit to 5 requests per minute
)


conn = connect("challenge.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        fortune TEXT NOT NULL
    );
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS flag (
        flag TEXT
    );
""")
cursor.execute("INSERT OR IGNORE INTO flag VALUES ('42HN{5ql1t3_t4bb5}');")
conn.commit()
conn.close()


@app.route('/',methods=["GET"])
def m():
    return render_template("index.html")



@app.route('/login', methods=["GET", "POST"])
@limiter.limit("10 per minute")
def index():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if " " in username or " " in password or re.search(r"/\*|\*/|LIKE", username) or re.search(r"/\*|\*/|LIKE", password):
            return "Hacking attempt detected!"


        conn = connect("challenge.db")
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)
        user = cursor.fetchone()
        conn.close()

        if user:
            return f"Welcome {username}! Your fortune: {user[2]}"
        else:
            return "Invalid credentials!"
    
    return render_template("index.html")


if __name__ == '__main__':
    app.run(port=3000, debug=False)
