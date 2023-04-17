from flask import Flask, request, jsonify

import cost_departments
import admin_costs
from item_costs import get_all_item_costs, get_item_cost, add_item_cost, update_item_cost, delete_item_cost
from staff_costs import get_all_staff_costs, get_staff_cost, add_staff_cost, update_staff_cost, delete_staff_cost

app = Flask(__name__)




@app.route("/admin_costs", methods=["GET"])
def get_admin_costs():
    result = admin_costs.get_all_admin_costs()
    return jsonify(result)

@app.route("/admin_costs/<int:id>", methods=["GET"])
@app.route("/admin_costs/name/<string:name>", methods=["GET"])
def get_admin_cost_route(id=None, name=None):
    result = admin_costs.get_admin_cost(id=id, name=name)
    if result:
        return jsonify(result)
    else:
        return jsonify({"message": "Admin cost not found"}), 404

@app.route("/admin_costs", methods=["POST"])
def add_admin_cost_route():
    data = request.get_json()
    name = data.get("name")
    price_cost = data.get("price_cost")
    department_id = data.get("department_id")
    admin_costs.add_admin_cost(name, price_cost, department_id)
    return jsonify({"message": "Admin cost added successfully"})

@app.route("/admin_costs/<int:id>", methods=["PUT"])
def update_admin_cost_route(id):
    data = request.get_json()
    name = data.get("name")
    price_cost = data.get("price_cost")
    department_id = data.get("department_id")
    admin_costs.update_admin_cost(id, name=name, price_cost=price_cost, department_id=department_id)
    return jsonify({"message": "Admin cost updated successfully"})

@app.route("/admin_costs/<int:id>", methods=["DELETE"])
def delete_admin_cost_route(id):
    admin_costs.delete_admin_cost(id)
    return jsonify({"message": "Admin cost deleted successfully"})
@app.route("/staff_costs", methods=["GET"])
def get_staff_costs():
    result = get_all_staff_costs()
    return jsonify(result)

@app.route("/staff_costs/<int:id>", methods=["GET"])
@app.route("/staff_costs/name/<string:name>", methods=["GET"])
def get_staff_cost_route(id=None, name=None):
    result = get_staff_cost(id=id, name=name)
    if result:
        return jsonify(result)
    else:
        return jsonify({"message": "Staff cost not found"}), 404

@app.route("/staff_costs", methods=["POST"])
def add_staff_cost_route():
    data = request.get_json()
    name = data.get("name")
    price_per_hour = data.get("price_per_hour")
    department_id = data.get("department_id")
    add_staff_cost(name, price_per_hour, department_id)
    return jsonify({"message": "Staff cost added successfully"})

@app.route("/staff_costs/<int:id>", methods=["PUT"])
def update_staff_cost_route(id):
    data = request.get_json()
    name = data.get("name")
    price_per_hour = data.get("price_per_hour")
    department_id = data.get("department_id")
    update_staff_cost(id, name=name, price_per_hour=price_per_hour, department_id=department_id)
    return jsonify({"message": "Staff cost updated successfully"})

@app.route("/staff_costs/<int:id>", methods=["DELETE"])
def delete_staff_cost_route(id):
    delete_staff_cost(id)
    return jsonify({"message": "Staff cost deleted successfully"})

@app.route("/item_costs", methods=["GET"])
def get_item_costs():
    result = get_all_item_costs()
    return jsonify(result)

@app.route("/item_costs/<int:id>", methods=["GET"])
@app.route("/item_costs/name/<string:name>", methods=["GET"])
def get_item_cost_route(id=None, name=None):
    result = get_item_cost(id=id, name=name)
    if result:
        return jsonify(result)
    else:
        return jsonify({"message": "Item cost not found"}), 404

@app.route("/item_costs", methods=["POST"])
def add_item_cost_route():
    data = request.get_json()
    name = data.get("name")
    price_per_item = data.get("price_per_item")
    department_id = data.get("department_id")
    add_item_cost(name, price_per_item, department_id)
    return jsonify({"message": "Item cost added successfully"})

@app.route("/item_costs/<int:id>", methods=["PUT"])
def update_item_cost_route(id):
    data = request.get_json()
    name = data.get("name")
    price_per_item = data.get("price_per_item")
    department_id = data.get("department_id")
    update_item_cost(id, name=name, price_per_item=price_per_item, department_id=department_id)
    return jsonify({"message": "Item cost updated successfully"})

@app.route("/item_costs/<int:id>", methods=["DELETE"])
def delete_item_cost_route(id):
    delete_item_cost(id)
    return jsonify({"message": "Item cost deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)
