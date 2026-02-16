from flask import session, redirect, url_for
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
app.secret_key = "hegde_art_space_secret"

def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/history")
def history():
    return render_template("history.html")


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


@app.route("/rules")
def rules():
    return render_template("rules.html")


@app.route("/booking")
def booking():
    return render_template("booking.html")


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    program = request.form["program"]
    phone = request.form["phone"]
    booking_date = request.form["booking_date"]
    charge = 21000

    conn = get_db_connection()
    conn.execute(
        "INSERT INTO bookings (name, program, phone, booking_date, charge) VALUES (?, ?, ?, ?, ?)",
        (name, program, phone, booking_date, charge)
    )
    conn.commit()
    conn.close()

    return render_template(
        "receipt.html",
        name=name,
        program=program,
        phone=phone,
        booking_date=booking_date,
        charge=charge
    )


@app.route("/db-test")
def db_test():
    conn = get_db_connection()
    conn.execute("SELECT 1")
    conn.close()
    return "SQLite Connected Successfully"


@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        admin = conn.execute(
            "SELECT * FROM admin_users WHERE username=? AND password=?",
            (username, password)
        ).fetchone()
        conn.close()

        if admin:
            session["admin_logged_in"] = True
            return redirect(url_for("admin_dashboard"))
        else:
            return "Invalid login"

    return render_template("admin_login.html")


@app.route("/admin/dashboard")
def admin_dashboard():
    if not session.get("admin_logged_in"):
        return redirect(url_for("admin_login"))

    conn = get_db_connection()
    bookings = conn.execute("SELECT * FROM bookings").fetchall()
    conn.close()

    return render_template("admin_dashboard.html", bookings=bookings)


@app.route("/admin/logout")
def admin_logout():
    session.clear()
    return redirect(url_for("admin_login"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
