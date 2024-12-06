from flask import Flask
from src.routes.cid_routes import init_routes
import os

template_dir = os.path.abspath("src/templates")
static_dir = os.path.abspath("src/static")

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

init_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
