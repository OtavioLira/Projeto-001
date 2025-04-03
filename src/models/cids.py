from src.connection import get_database
import json
from flask import Response, jsonify

db = get_database()
cid_collection = db["lista_cids"]

def get_all():
    try:
        cids = list(cid_collection.find({}, {"_id": 0})).sort()
        return jsonify(cids)
    except Exception as e:
        return jsonify({"error": f"Erro ao acessar o banco de dados: {e}"}), 500

def get_cid_by_cod(codigo):
    try:
        cid = cid_collection.find_one({"codigo": codigo}, {"_id": 0}).sort()
        return jsonify(cid) if cid else jsonify({"error": "CID não encontrado!"}), 404
    except Exception as e:
        return jsonify({"error": f"Erro ao acessar o banco de dados: {e}"}), 500

def get_cid_by_name(nome):
    try:
        cid = cid_collection.find_one({"nome": nome}, {"_id": 0}).sort()
        return jsonify(cid) if cid else jsonify({"message": "Nenhum CID encontrado com o nome especificado"}), 404
    except Exception as e:
        return jsonify({"error": f"Erro ao acessar o banco de dados: {e}"}), 500

def get_cid_by_range(start_range, end_range):
    try:
        cids = list(cid_collection.find({"codigo": {"$gte": start_range, "$lte": end_range}}, {"_id": 0}))
        return jsonify(cids) if cids else jsonify({"message": "Nenhum CID encontrado no intervalo especificado"}), 404
    except Exception as e:
        return jsonify({"error": f"Erro ao acessar o banco de dados: {e}"}), 500
