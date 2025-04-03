from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from src.routes.auth_routes import auth_bp
from src.routes.cid_routes import cid_bp
import os

template_dir = os.path.abspath("src/templates")
static_dir = os.path.abspath("src/static")

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")

jwt = JWTManager(app)

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(cid_bp, url_prefix="/api")

@app.route("/")
def main_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
