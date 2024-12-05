from flask import request, jsonify
from src.connection import get_database

db = get_database()
cid_collection = db["lista_cids"]

def init_routes(app):
    @app.route("/")
    def main():
        return "<h1>API LIRA CIDS</h1>"

    # Rota para criar um novo CID
    @app.route("/cids", methods=["POST"])
    def create_cid():
        try:
            data = request.json
            if "codigo" not in data or "nome" not in data:
                return jsonify({"error": "Os campos 'codigo' e 'nome' são obrigatórios!"}), 400
            
            cid = {
                "codigo": data["codigo"],
                "nome": data["nome"],
                "categoria": data.get("categoria", ""),
            }
            cid_collection.insert_one(cid)
            return jsonify({"message": "CID criado com sucesso!"}), 201
        except Exception as e:
            print(f"Erro ao acessar o banco de dados: {e}")
            return jsonify({"error": "Erro ao acessar o banco de dados"}), 500
        
    # Rota para listar todos os CIDs
    @app.route("/cids", methods=["GET"])
    def get_all_cids():
        try:
            cids = list(cid_collection.find({}, {"_id": 0}))
            return jsonify(cids), 200
        except Exception as e:
            print(f"Erro ao acessar o banco de dados: {e}")
            return jsonify({"error": "Erro ao acessar o banco de dados"}), 500

    # Rota para buscar um CID por código
    @app.route("/cids/<string:codigo>", methods=["GET"])
    def get_cid_by_codigo(codigo):
        try:
            cid = cid_collection.find_one({"codigo": codigo}, {"_id": 0})
            if cid:
                return jsonify(cid), 200
            return jsonify({"error": "CID não encontrado!"}), 404
        except Exception as e:
            print(f"Erro ao acessar o banco de dados: {e}")
            return jsonify({"error": "Erro ao acessar o banco de dados"}), 500
        
    # Rota para atualizar um CID
    @app.route("/cids/<string:codigo>", methods=["PUT"])
    def update_cid(codigo):
        try:
            data = request.json
            result = cid_collection.update_one({"codigo": codigo}, {"$set": data})
            if result.matched_count > 0:
                return jsonify({"message": "CID atualizado com sucesso!"}), 200
            return jsonify({"error": "CID não encontrado!"}), 404
        except Exception as e:
            print(f"Erro ao acessar o banco de dados: {e}")
            return jsonify({"error": "Erro ao acessar o banco de dados"}), 500
        
    # Rota para deletar um CID
    @app.route("/cids/<string:codigo>", methods=["DELETE"])
    def delete_cid(codigo):
        try:
            result = cid_collection.delete_one({"codigo": codigo})
            if result.deleted_count > 0:
                return jsonify({"message": "CID deletado com sucesso!"}), 200
            return jsonify({"error": "CID não encontrado!"}), 404
        except Exception as e:
            print(f"Erro ao acessar o banco de dados: {e}")
            return jsonify({"error": "Erro ao acessar o banco de dados"}), 500       