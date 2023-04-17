import mysql.connector
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dr980512",
        database="clinical_trial_units"
    )
def get_all_cost_departments():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM cost_departments")
    result = cursor.fetchall()
    conn.close()
    return result

def get_all_cost_department(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM cost_departments WHERE id=%s", (id,))
    result = cursor.fetchone()
    conn.close()
    return result

def add_cost_department(department):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cost_departments (department) VALUES (%s)", (department,))
    conn.commit()
    conn.close()

def update_cost_department(id, department):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE cost_departments SET department=%s WHERE id=%s", (department, id))
    conn.commit()
    conn.close()

def delete_cost_department(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cost_departments WHERE id=%s", (id,))
    conn.commit()
    conn.close()


from flask import Flask, request, jsonify
from app import app
@app.route("/cost_departments", methods=["GET"])
def get_cost_departments():
    result = get_all_cost_departments()
    return jsonify(result)

@app.route("/cost_departments/<int:id>", methods=["GET"])
def get_cost_department_route(id):
    result = get_all_cost_department(id)
    if result:
        return jsonify(result)
    else:
        return jsonify({"message": "Department not found"}), 404

@app.route("/cost_departments", methods=["POST"])
def add_cost_department_route():
    data = request.get_json()
    department = data.get("department")
    add_cost_department(department)
    return jsonify({"message": "Department added successfully"})

@app.route("/cost_departments/<int:id>", methods=["PUT"])
def update_cost_department_route(id):
    data = request.get_json()
    department = data.get("department")
    update_cost_department(id, department)
    return jsonify({"message": "Department updated successfully"})

@app.route("/cost_departments/<int:id>", methods=["DELETE"])
def delete_cost_department_route(id):
    delete_cost_department(id)
    return jsonify({"message": "Department deleted successfully"})