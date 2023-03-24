import mysql.connector

def connection():
    db=mysql.connector.connect(
        host='localhost',
        user='root',
        password='Tout@52'
    )

    print("\nServer Connected....\n")

    return db

# connection()