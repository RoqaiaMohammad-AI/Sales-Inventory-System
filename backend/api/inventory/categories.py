from flask import Blueprint, jsonify, request

from services.inventory.category_service import (
    get_all_categories,
    get_category_by_id,
    create_category,
    update_category,
    delete_category,
)


categories_bp = Blueprint(
    "categories",
    __name__,
    url_prefix="/api/categories",
)


def serialize_category(category):
    return {
        "id": category.id,
        "name": category.name,
        "description": category.description,
        "created_at": (
            category.created_at.isoformat()
            if category.created_at else None
        ),
    }


@categories_bp.get("/")
def list_categories():
    categories = get_all_categories()

    return jsonify({
        "success": True,
        "data": [serialize_category(item) for item in categories],
    }), 200


@categories_bp.get("/<int:category_id>")
def get_category(category_id):
    category = get_category_by_id(category_id)

    if category is None:
        return jsonify({
            "success": False,
            "message": "التصنيف غير موجود.",
        }), 404

    return jsonify({
        "success": True,
        "data": serialize_category(category),
    }), 200


@categories_bp.post("/")
def add_category():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "success": False,
            "message": "يجب إرسال بيانات بصيغة JSON.",
        }), 400

    name = data.get("name")
    description = data.get("description")

    if not isinstance(name, str) or not name.strip():
        return jsonify({
            "success": False,
            "message": "اسم التصنيف مطلوب.",
        }), 400

    if len(name.strip()) > 120:
        return jsonify({
            "success": False,
            "message": "اسم التصنيف يجب ألا يتجاوز 120 حرفًا.",
        }), 400

    if description is not None and not isinstance(description, str):
        return jsonify({
            "success": False,
            "message": "الوصف يجب أن يكون نصًا.",
        }), 400

    try:
        category = create_category(name, description)

        return jsonify({
            "success": True,
            "message": "تم إنشاء التصنيف بنجاح.",
            "data": serialize_category(category),
        }), 201

    except ValueError as error:
        return jsonify({
            "success": False,
            "message": str(error),
        }), 409


@categories_bp.put("/<int:category_id>")
def edit_category(category_id):
    category = get_category_by_id(category_id)

    if category is None:
        return jsonify({
            "success": False,
            "message": "التصنيف غير موجود.",
        }), 404

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "success": False,
            "message": "يجب إرسال بيانات بصيغة JSON.",
        }), 400

    name = data.get("name")
    description = data.get("description")

    if not isinstance(name, str) or not name.strip():
        return jsonify({
            "success": False,
            "message": "اسم التصنيف مطلوب.",
        }), 400

    if len(name.strip()) > 120:
        return jsonify({
            "success": False,
            "message": "اسم التصنيف يجب ألا يتجاوز 120 حرفًا.",
        }), 400

    if description is not None and not isinstance(description, str):
        return jsonify({
            "success": False,
            "message": "الوصف يجب أن يكون نصًا.",
        }), 400

    try:
        category = update_category(category, name, description)

        return jsonify({
            "success": True,
            "message": "تم تحديث التصنيف بنجاح.",
            "data": serialize_category(category),
        }), 200

    except ValueError as error:
        return jsonify({
            "success": False,
            "message": str(error),
        }), 409


@categories_bp.delete("/<int:category_id>")
def remove_category(category_id):
    category = get_category_by_id(category_id)

    if category is None:
        return jsonify({
            "success": False,
            "message": "التصنيف غير موجود.",
        }), 404

    delete_category(category)

    return jsonify({
        "success": True,
        "message": "تم حذف التصنيف بنجاح.",
    }), 200
