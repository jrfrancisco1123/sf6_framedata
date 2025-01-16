from flask_app import app
from flask import render_template

# MAIN PAGE
@app.route('/')
def index():
    return render_template('index.html')

# DASHBOARD
@app.route('/sf6_framedata/dashboard')
def dashboard():
    return render_template('dashboard.html')