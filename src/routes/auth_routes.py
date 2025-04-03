from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from src.models.users import UserModel

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if UserModel.find_user_by_username(data["username"]):
        return jsonify({"message": "Usuário já existe"}), 400
    
    UserModel.create_user(data["username"], data["email"], data["password"])
    return jsonify({"message": "Usuário registrado"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = UserModel.find_user_by_username(data["username"])

    if not user or not UserModel.verify_password(data["password"], user["password"]):
        return jsonify({"message": "Credenciais inválidas"}), 401
    
    access_token = create_access_token(identity=user["username"])
    return jsonify({"token": access_token}), 200
