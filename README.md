# Hegde Art Space 🎶💃

An online booking system for music and dance programs, built using **Python (Flask)**, **HTML**, **CSS**.  
This project allows users to book Hindustani, Carnatic, and dance programs, and generates a booking receipt.  

## Features
 * Home page with project overview
 *  Booking page with calendar for selecting date
 *  Fixed charge per day: ₹21,000
 *  Booking receipt generation with Name, Program, Phone, Date, and Charge
 *  About, History, Gallery, and Rules pages
 *  Admin-only booking history (planned feature)
 *  Prevent booking for already booked dates (planned feature)  

## Project Structure
Hegde_art_space/
│
├─ app.py # Flask application
├─ bookings.csv # Stores all booking data (ignored on GitHub)
├─ static/
│ └─ style.css # CSS styles
├─ templates/
│ ├─ index.html
│ ├─ booking.html
│ ├─ receipt.html
│ ├─ about.html
│ ├─ gallery.html
│ ├─ rules.html
│ ├─ history.html
│ ├─ success.html
│ └─ template.html
├─ .gitignore # Ignores venv, CSV, pycache
└─ README.md # Project documentation


---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Hegdesubrahmanya/Hegde_art_space.git
cd Hegde_art_space

Create a virtual environment and activate it:
python3 -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows


Install dependencies:
pip install flask

Run the app:
python app.py
