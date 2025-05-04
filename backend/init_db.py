import mysql.connector

# database configuration
DB_CONFIG = {
    "host": "mysql",
    "user": "root",
    "password": "root",
    "database": "benchai"
}

def init_database():
    # connect to mysql server
    conn = mysql.connector.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"]
    )
    cursor = conn.cursor()

    try:
        # create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS benchai")
        cursor.execute("USE benchai")

        # create users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) UNIQUE NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                hashed_password VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        conn.commit()
        print("Database and tables initialized successfully!")
    except Exception as e:
        print(f"Error initializing database: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    init_database() 