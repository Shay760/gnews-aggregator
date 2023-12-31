# models.py
from flask_pymongo import PyMongo
from flask import current_app

mongo = PyMongo(app)

# Define the News model
class News:
    @staticmethod
    def get_all():
        return list(mongo.db.news.find())

    @staticmethod
    def create(title, content, author):
        return mongo.db.news.insert_one({
            'title': title,
            'content': content,
            'author': author,
        })

# Define the UserInteraction model
class UserInteraction:
    @staticmethod
    def create(user_id, news_id, interaction_type):
        return mongo.db.user_interaction.insert_one({
            'user_id': user_id,
            'news_id': news_id,
            'interaction_type': interaction_type,
        })
