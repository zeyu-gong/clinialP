import mysql.connector

def connect_to_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dr980512",
        database="clinical_trial_units"
    )
    return connection

def get_all_staff_costs():
    connection = connect_to_db()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM staff_costs")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def get_staff_cost(id=None, name=None):
    connection = connect_to_db()
    cursor = connection.cursor(dictionary=True)
    if id:
        cursor.execute("SELECT * FROM staff_costs WHERE id = %s", (id,))
    elif name:
        cursor.execute("SELECT * FROM staff_costs WHERE name = %s", (name,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result

def add_staff_cost(name, price_per_hour, department_id):
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO staff_costs (name, price_per_hour, department_id) VALUES (%s, %s, %s)",
                   (name, price_per_hour, department_id))
    connection.commit()
    cursor.close()
    connection.close()

def update_staff_cost(id, name=None, price_per_hour=None, department_id=None):
    connection = connect_to_db()
    cursor = connection.cursor()
    if name:
        cursor.execute("UPDATE staff_costs SET name = %s WHERE id = %s", (name, id))
    if price_per_hour:
        cursor.execute("UPDATE staff_costs SET price_per_hour = %s WHERE id = %s", (price_per_hour, id))
    if department_id:
        cursor.execute("UPDATE staff_costs SET department_id = %s WHERE id = %s", (department_id, id))
    connection.commit()
    cursor.close()
    connection.close()

def delete_staff_cost(id):
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM staff_costs WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()