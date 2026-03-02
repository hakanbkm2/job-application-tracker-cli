import mysql.connector

def connect_db():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="job_tracker"
    )
    
    return db