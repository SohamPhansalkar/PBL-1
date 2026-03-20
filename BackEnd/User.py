import mysql.connector
from encrypt import encrypt_password

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="pbl1"
    )

def signUp(email, password):
    hashed_password = encrypt_password(password)
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = "INSERT INTO user (email, password) VALUES (%s, %s)"
        cursor.execute(query, (email, hashed_password))
        conn.commit()
        return {"status": "success", "message": "User created successfully"}
    except mysql.connector.Error as err:
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()
        conn.close()

def logIn(email, password):
    hashed_input = encrypt_password(password)
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    query = "SELECT password FROM user WHERE email = %s"
    cursor.execute(query, (email,))
    user = cursor.fetchone()
    
    cursor.close()
    conn.close()

    if user:
        if user['password'] == hashed_input:
            return {"status": "success", "message": "Login successful"}
        
        return {"status": "error", "message": "Invalid password"}
    return {"status": "error", "message": "User not found"}