from flask import Flask
from src.routes.cid_routes import init_routes
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

PORT = os.environ["PORT"]

init_routes(app)

if __name__ == "__main__":
    app.run(debug=True, PORT=PORT)
