from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Shikha@1407@localhost/wedding_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    venue = db.Column(db.String(200), nullable=False)
    theme = db.Column(db.String(100), nullable=False)
    schedule = db.Column(db.Date, nullable=False)

class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(100), nullable=False)
    contract_details = db.Column(db.Text, nullable=False)

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    rsvp_status = db.Column(db.String(10), nullable=False)

class Budget(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_event', methods=['POST'])
def add_event():
    if request.method == 'POST':
        name = request.form['event-name']
        venue = request.form['venue']
        theme = request.form['theme']
        schedule = request.form['schedule']

        new_event = Event(name=name, venue=venue, theme=theme, schedule=schedule)
        db.session.add(new_event)
        db.session.commit()
        flash('Event created successfully!', 'success')
        return redirect(url_for('index'))

@app.route('/add_vendor', methods=['POST'])
def add_vendor():
    if request.method == 'POST':
        name = request.form['vendor-name']
        service_type = request.form['service']
        contract_details = request.form['contract']

        new_vendor = Vendor(name=name, service_type=service_type, contract_details=contract_details)
        db.session.add(new_vendor)
        db.session.commit()
        flash('Vendor added successfully!', 'success')
        return redirect(url_for('index'))

@app.route('/add_guest', methods=['POST'])
def add_guest():
    if request.method == 'POST':
        name = request.form['guest-name']
        rsvp_status = request.form['rsvp']

        new_guest = Guest(name=name, rsvp_status=rsvp_status)
        db.session.add(new_guest)
        db.session.commit()
        flash('Guest added successfully!', 'success')
        return redirect(url_for('index'))

@app.route('/add_budget', methods=['POST'])
def add_budget():
    if request.method == 'POST':
        category = request.form['category']
        amount = request.form['amount']

        new_budget = Budget(category=category, amount=float(amount))
        db.session.add(new_budget)
        db.session.commit()
        flash('Expense added successfully!', 'success')
        return redirect(url_for('index'))

# Create tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
