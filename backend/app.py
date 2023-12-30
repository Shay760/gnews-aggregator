from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os 

load_dotenv() # Load environment variables from .env file 

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configuration settings
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key')

# MongoDB Database Connection 
client = MongoClient(os.environ.get("MONGODB_URI", "mongodb://localhost:27017"))
db = client.get_default_database()


# Example route to get general gaming news
@app.route('/api/news', methods=['GET'])
def get_general_news():
    # Logic to fetch and return general gaming news
    return jsonify({'message': 'General gaming news data'})

# Example route to get specific news based on news_id
@app.route('/api/news/<int:news_id>', methods=['GET'])
def get_specific_news(news_id):
    # Logic to fetch and return specific news based on news_id
    return jsonify({'message': f'News data for ID {news_id}'})

# Example route to create new news
@app.route('/api/news', methods=['POST'])
def create_news():
    # Logic to create new news based on frontend request
    return jsonify({'message': 'News created'})

# Example route to update user preferences
@app.route('/api/user/preferences', methods=['POST'])
def update_user_preferences():
    # Logic to update user preferences based on frontend request
    return jsonify({'message': 'User preferences updated'})

# Add more routes and functionality as needed

if __name__ == "__main__":
    app.run(debug=True)
