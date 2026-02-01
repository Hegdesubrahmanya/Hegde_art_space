from flask import Flask, render_template, request

app = Flask(__name__)

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

    # SAVE booking to file
    with open("bookings.csv", "a") as file:
        file.write(f"{name},{program},{phone},{booking_date},{charge}\n")

    return render_template(
        "receipt.html",
        name=name,
        program=program,
        phone=phone,
        booking_date=booking_date,
        charge=charge
    )

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/history")
def booking_history():
    bookings = []

    with open("bookings.csv", "r") as file:
        lines = file.readlines()[1:]  # skip header
        for line in lines:
            bookings.append(line.strip().split(","))

    return render_template("booking_history.html", bookings=bookings)
