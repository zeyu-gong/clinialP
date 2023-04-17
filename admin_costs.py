import mysql.connector
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dr980512",
        database="clinical_trial_units"
    )

def get_all_admin_costs():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM admin_costs")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def get_admin_cost(id=None, name=None):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    if id:
        cursor.execute("SELECT * FROM admin_costs WHERE id = %s", (id,))
    elif name:
        cursor.execute("SELECT * FROM admin_costs WHERE name = %s", (name,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result

def add_admin_cost(name, price_cost, department_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO admin_costs (name, price_cost, department_id) VALUES (%s, %s, %s)",
                   (name, price_cost, department_id))
    connection.commit()
    cursor.close()
    connection.close()

def update_admin_cost(id, name=None, price_cost=None, department_id=None):
    connection = get_db_connection()
    cursor = connection.cursor()
    if name:
        cursor.execute("UPDATE admin_costs SET name = %s WHERE id = %s", (name, id))
    if price_cost:
        cursor.execute("UPDATE admin_costs SET price_cost = %s WHERE id = %s", (price_cost, id))
    if department_id:
        cursor.execute("UPDATE admin_costs SET department_id = %s WHERE id = %s", (department_id, id))
    connection.commit()
    cursor.close()
    connection.close()

def delete_admin_cost(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM admin_costs WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()