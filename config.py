import mysql.connector 

# Configuración de conexión
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "ali123", 
    "database": "CentroAdopcion"
}

def get_db_connection():
    try:
        # Aquí también cambiamos mariadb.connect por mysql.connector.connect
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as e:
        print(f"Error conectando a MySQL: {e}")
        return None