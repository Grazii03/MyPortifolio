from flask import Flask, send_from_directory
from pathlib import Path

from backend.routes.skills_routes import skills_bp
from backend.models.db import init_db

app = Flask(__name__)
app.register_blueprint(skills_bp)

# caminho absoluto da raiz do projeto
BASE_DIR = Path(__file__).resolve().parents[2]   # .../MyPortifolio
FRONTEND_DIR = BASE_DIR / "frontend"
ASSETS_DIR = FRONTEND_DIR / "assets"

@app.get("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")

@app.get("/assets/<path:filename>")
def assets(filename):
    return send_from_directory(ASSETS_DIR, filename)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)