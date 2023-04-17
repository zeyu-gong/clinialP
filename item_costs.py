import mysql.connector

def connect_to_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dr980512",
        database="clinical_trial_units"
    )
    return connection

def get_all_item_costs():
    connection = connect_to_db()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM item_costs")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def get_item_cost(id=None, name=None):
    connection = connect_to_db()
    cursor = connection.cursor(dictionary=True)
    if id:
        cursor.execute("SELECT * FROM item_costs WHERE id = %s", (id,))
    elif name:
        cursor.execute("SELECT * FROM item_costs WHERE name = %s", (name,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result

def add_item_cost(name, price_per_item, department_id):
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO item_costs (name, price_per_item, department_id) VALUES (%s, %s, %s)",
                   (name, price_per_item, department_id))
    connection.commit()
    cursor.close()
    connection.close()

def update_item_cost(id, name=None, price_per_item=None, department_id=None):
    connection = connect_to_db()
    cursor = connection.cursor()
    if name:
        cursor.execute("UPDATE item_costs SET name = %s WHERE id = %s", (name, id))
    if price_per_item:
        cursor.execute("UPDATE item_costs SET price_per_item = %s WHERE id = %s", (price_per_item, id))
    if department_id:
        cursor.execute("UPDATE item_costs SET department_id = %s WHERE id = %s", (department_id, id))
    connection.commit()
    cursor.close()
    connection.close()

def delete_item_cost(id):
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM item_costs WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()