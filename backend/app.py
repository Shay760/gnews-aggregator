# app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
from models import News, UserInteraction

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'default_secret_key'

# No need to initialize MongoClient, use the PyMongo instance
# client = MongoClient(os.environ.get("MONGODB_URI", "mongodb://localhost:27017/gaming_news_aggregator"))
# db = client.get_default_database()

# Use the PyMongo instance from models.py
from models import mongo

# Example route to get general gaming news
@app.route('/api/news', methods=['GET'])
def get_general_news():
    news_data = News.get_all()
    return jsonify({'news': news_data})

# Example route to update user preferences
@app.route('/api/user/preferences', methods=['POST'])
def update_user_preferences():
    user_interaction = UserInteraction.create(user_id='user123', news_id='news456', interaction_type='like')
    return jsonify({'message': 'User preferences updated'})

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
@app.route('/api/user/preferences/other', methods=['POST'])
def update_user_preferences():
    # Logic to update user preferences based on frontend request
    return jsonify({'message': 'User preferences updated'})

# Add more routes and functionality as needed

if __name__ == "__main__":
    app.run(debug=True)
