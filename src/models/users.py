from src.connection import get_database
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
db = get_database()
user_collection = db["users"]

class UserModel():
    @staticmethod
    def create_user(username, email, password):
        hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")
        user = {"username": username, "email": email, "password": hashed_pw}
        user_collection.insert_one(user)

    @staticmethod
    def find_user_by_username(username):
        return user_collection.find_one({"username": username})

    @staticmethod
    def verify_password(password, hashed_password):
        return bcrypt.check_password_hash(hashed_password, password)
