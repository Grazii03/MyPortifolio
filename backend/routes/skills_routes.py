from flask import Blueprint, jsonify
from backend.controllers.skills_controller import list_skills

skills_bp = Blueprint("skills_bp", __name__)

@skills_bp.get("/api/skills")
def get_skills():
    return jsonify(list_skills())