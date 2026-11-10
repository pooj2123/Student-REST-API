from flask import Flask, request, jsonify

app = Flask(__name__)

# Temporary in-memory student records
students = {
    1: {"id": 1, "name": "Arjun", "age": 20, "course": "CSE"},
    2: {"id": 2, "name": "Priya", "age": 21, "course": "ECE"}
}

@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(list(students.values())), 200

@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    student = students.get(student_id)
    if student is None:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(student), 200

@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()
    if not data or not all(key in data for key in ["name", "age", "course"]):
        return jsonify({"error": "Send name, age and course"}), 400

    new_id = max(students.keys(), default=0) + 1
    student = {
        "id": new_id,
        "name": data["name"],
        "age": data["age"],
        "course": data["course"]
    }
    students[new_id] = student
    return jsonify(student), 201

@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    if student_id not in students:
        return jsonify({"error": "Student not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Send JSON data"}), 400

    students[student_id]["name"] = data.get("name", students[student_id]["name"])
    students[student_id]["age"] = data.get("age", students[student_id]["age"])
    students[student_id]["course"] = data.get("course", students[student_id]["course"])
    return jsonify(students[student_id]), 200

@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    if student_id not in students:
        return jsonify({"error": "Student not found"}), 404

    deleted_student = students.pop(student_id)
    return jsonify({
        "message": "Student deleted successfully",
        "student": deleted_student
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
