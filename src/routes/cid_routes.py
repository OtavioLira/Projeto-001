from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from src.models import cids

cid_bp = Blueprint("cid", __name__)

# Rota para listar todos os CIDs
@cid_bp.route("/cids", methods=["GET"])
@jwt_required()
def get_all_cids():
    return cids.get_all()

# Rota para buscar um CID por código
@cid_bp.route("/cids/codigo/<string:codigo>", methods=["GET"])
@jwt_required()
def get_cid_by_cod(codigo):
    return cids.get_cid_by_cod(codigo)

# Rota para buscar uma lista de CIDs filtrados por intervalo de códigos
@cid_bp.route("/cids/<string:start_range>:<string:end_range>", methods=["GET"])
@jwt_required()
def get_cid_by_range(start_range, end_range):
    return cids.get_cid_by_range(start_range, end_range)

# Rota para buscar um CID pelo nome da doença
@cid_bp.route("/cids/nome/<string:nome>", methods=["GET"])
@jwt_required()
def get_cid_by_name(nome):
    return cids.get_cid_by_name(nome)
