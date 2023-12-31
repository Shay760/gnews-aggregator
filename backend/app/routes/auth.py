# auth.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Wayne'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.template_folder = 'templates'

# Configure MongoDB using Flask-PyMongo
app.config['MONGO_URI'] = 'mongodb://localhost:27017/gaming_news_aggregator'
mongo = PyMongo(app)

# Remove the following lines related to Flask-MongoEngine
# db = MongoEngine(app)  # Initialize the MongoEngine extension

# Define a registration form
class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Register')

# Create a registration route
# Renders the registration form and handles form submission
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        # Logic to handle registration using MongoDB (Flask-PyMongo)
        flash('Registration successful!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

# Define a login form 
class LoginForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('Password', [validators.DataRequired()])
    submit = SubmitField('Login')

# Create a login route 
# Renders the login form and handles form submissions 
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # Logic to handle login (without database connection for now)
        flash('Login successful!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('login.html', form=form)

# auth.py (continued)
if __name__ == "__main__":
    app.run(debug=True, port=5001)
