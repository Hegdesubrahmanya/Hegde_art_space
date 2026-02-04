from flask import session, redirect, url_for
from flask import Flask, render_template, request

# 🔹 ADDED: MySQL import
import mysql.connector

app = Flask(__name__)
app.secret_key = "hegde_art_space_secret"

# 🔹 ADDED: MySQL connection
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root123",
    database="hegde_art_space",
    port=3307
)

# 🔹 ADDED: Cursor
cursor = db.cursor(dictionary=True)


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

    cursor.execute(
        "INSERT INTO bookings (name, program, phone, booking_date, charge) VALUES (%s, %s, %s, %s, %s)",
        (name, program, phone, booking_date, charge)
    )
    db.commit()

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
    cursor.execute("SELECT DATABASE();")
    result = cursor.fetchone()
    return f"Connected to DB: {result}"

@app.route("/history")
def booking_history():
    bookings = []

    with open("bookings.csv", "r") as file:
        lines = file.readlines()[1:]  # skip header
        for line in lines:
            bookings.append(line.strip().split(","))

    return render_template("booking_history.html", bookings=bookings)

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        cursor.execute(
            "SELECT * FROM admin_users WHERE username=%s AND password=%s",
            (username, password)
        )
        admin = cursor.fetchone()

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

    cursor.execute("SELECT * FROM bookings")
    bookings = cursor.fetchall()

    return render_template("admin_dashboard.html", bookings=bookings)

@app.route("/admin/logout")
def admin_logout():
    session.clear()
    return redirect(url_for("admin_login"))

if __name__ == "__main__":
    app.run(debug=True)