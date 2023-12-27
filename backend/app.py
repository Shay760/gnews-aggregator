from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def home():
    return 'Welcome to the Gaming News Aggregator API!'

# Add more routes and functionality as needed

if __name__ == "__main__":
    app.run(debug=True)
