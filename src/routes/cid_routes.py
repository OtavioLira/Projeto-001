from flask import request, jsonify, Response, render_template
import json
from src.connection import get_database

db = get_database()
cid_collection = db["lista_cids"]

def init_routes(app):
    @app.route("/")
    def main():
        return render_template("index.html")

    # # Rota para criar um novo CID
    # @app.route("/cids", methods=["POST"])
    # def create_cid():
    #     try:
    #         data = request.json
    #         if "codigo" not in data or "nome" not in data:
    #             return jsonify({"error": "Os campos 'codigo' e 'nome' são obrigatórios!"}), 400
            
    #         cid = {
    #             "codigo": data["codigo"],
    #             "nome": data["nome"],
    #             "categoria": data.get("categoria", ""),
    #         }
    #         cid_collection.insert_one(cid)
    #         return jsonify({"message": "CID criado com sucesso!"}), 201
    #     except Exception as e:
    #         print(f"Erro ao acessar o banco de dados: {e}")
    #         return jsonify({"error": "Erro ao acessar o banco de dados"}), 500
        
    # Rota para listar todos os CIDs
    @app.route("/cids", methods=["GET"])
    def get_all_cids():
        try:
            cids = list(cid_collection.find({}, {"_id": 0}))
            formatted_json = json.dumps(cids, ensure_ascii=False, indent=4)
            return Response(formatted_json, content_type="application/json")
        except Exception as e:
            print(f"Erro ao acessar o banco de dados: {e}")
            return jsonify({"error": "Erro ao acessar o banco de dados"}), 500

    # Rota para buscar um CID por código
    @app.route("/cids/codigo/<string:codigo>", methods=["GET"])
    def get_cid_by_codigo(codigo):
        try:
            cid = cid_collection.find_one({"codigo": codigo}, {"_id": 0})
            if cid:
                formatted_json = json.dumps(cid, ensure_ascii=False, indent=4)
                return Response(formatted_json, content_type="application/json")
            return jsonify({"error": "CID não encontrado!"}), 404
        except Exception as e:
            print(f"Erro ao acessar o banco de dados: {e}")
            return jsonify({"error": "Erro ao acessar o banco de dados"}), 500
        
    @app.route("/cids/<string:start_range>:<string:end_range>", methods=["GET"])
    def get_cid_by_range(start_range, end_range):
        try:
            cids = list(cid_collection.find(
                {"codigo": {"$gte": start_range, "$lte": end_range}}, 
                {"_id": 0}
            ))
            if not cids:
                return jsonify({"message": "Nenhum CID encontrado no intervalo especificado."}), 404
            formatted_json = json.dumps(cids, ensure_ascii=False, indent=4)
            return Response(formatted_json, content_type="application/json")
        except Exception as e:
            print(f"Erro ao acessar o banco de dados: {e}")
            return jsonify({"error": "Erro ao acessar o banco de dados"}), 500

    @app.route("/cids/nome/<string:nome>")
    def get_cid_by_name(nome):
        try:
            cid = cid_collection.find_one({"nome": nome}, {"_id": 0})
            if not cid:
                return jsonify({"message":f"Nenhum CID encontrado com o nome especificado"}), 404
            formatted_json = json.dumps(cid, ensure_ascii=False, indent=4)
            return Response(formatted_json, content_type="application/json")
        except Exception as e:
            print(f"Erro ao acessar o banco de dados: {e}")
            return jsonify({"error": "Erro ao acessar o banco de dados"}), 500     
           
    # Rota para atualizar um CID
    # @app.route("/cids/<string:codigo>", methods=["PUT"])
    # def update_cid(codigo):
    #     try:
    #         data = request.json
    #         result = cid_collection.update_one({"codigo": codigo}, {"$set": data})
    #         if result.matched_count > 0:
    #             return jsonify({"message": "CID atualizado com sucesso!"}), 200
    #         return jsonify({"error": "CID não encontrado!"}), 404
    #     except Exception as e:
    #         print(f"Erro ao acessar o banco de dados: {e}")
    #         return jsonify({"error": "Erro ao acessar o banco de dados"}), 500
        
    # # Rota para deletar um CID
    # @app.route("/cids/<string:codigo>", methods=["DELETE"])
    # def delete_cid(codigo):
    #     try:
    #         result = cid_collection.delete_one({"codigo": codigo})
    #         if result.deleted_count > 0:
    #             return jsonify({"message": "CID deletado com sucesso!"}), 200
    #         return jsonify({"error": "CID não encontrado!"}), 404
    #     except Exception as e:
    #         print(f"Erro ao acessar o banco de dados: {e}")
    #         return jsonify({"error": "Erro ao acessar o banco de dados"}), 500       