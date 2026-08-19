from flask import Blueprint, request, jsonify
from slugify import slugify
from db import get_connection

course_bp = Blueprint('course', __name__)

@course_bp.route('/courses', methods=['GET'])
def course():
    data = request.get_json()

    title = data.get('title')
    price = data.get('price', 0)
    currency = data.get('currency', 'NGN')
    free_count = data.get('free_count', 1)
    slug = slugify(title)

    if not title:
        return jsonify({"success": False, "message": "Title is required"}), 400
    if not currency:
        return jsonify({"success": False, "message": "Currency is required"}), 400
    if price <= 0:
        return jsonify({"success": False, "message": "Price cannot be negative"}), 400
    
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(""" SELECT * FROM Courses WHERE id = %s """, (data.get('id'),))
        conn.commit()
    except Exception as e:
        return jsonify({"error": e})

    print(data)
    return jsonify({ "Welcome to the Courses"}) 
    