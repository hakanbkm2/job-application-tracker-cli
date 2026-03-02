from database import connect_db
import mysql.connector
import csv
from database import connect_db

def test_connection():
   try:
    db = connect_db()
    
    if db.is_connected():
        print("Bağlantı başarılı.")
        
        cursor = db.cursor()
        cursor.execute("SELECT DATABASE();")
        
        result = cursor.fetchone()
        
        print("Bağlı olunan database:", result)

        cursor.close()
        db.close()

   except mysql.connector.Error as err:
    print("Hata oluştu:", err)

def add_application(company,position,salary,application_status,date_applied,job_link,notes):
    db = connect_db()
    cursor = db.cursor()
    query = """INSERT INTO applications(company,position,salary,application_status,date_applied,job_link,notes)
    VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    values = (company,position,salary,application_status,date_applied,job_link,notes)
    cursor.execute(query,values)
    db.commit()
    cursor.close()
    db.close()

def list_applications():
   db = connect_db()
   cursor = db.cursor(dictionary=True)

   query = "SELECT * FROM applications order by id desc"
   cursor.execute(query)

   results = cursor.fetchall()

   cursor.close()
   db.close()

   return results

def update_application_status(app_id, new_status):
   db = connect_db()
   cursor = db.cursor()
   query = "UPDATE applications SET application_status = %s where id = %s"
   values = (new_status,app_id)
   cursor.execute(query,values)
   db.commit()
   print(f"Application {app_id} Status updated to  {new_status}")
   cursor.close()
   db.close()

def delete_application(app_id):
   db = connect_db()
   cursor = db.cursor()
   query = "DELETE from applications where id = %s"
   value = (app_id,)
   cursor.execute(query,value)
   db.commit()
   if cursor.rowcount == 0 :
      print("Application not found.")
   else:
      print(f"Application {app_id} Deleted Succesfully")
   cursor.close()
   db.close()

def get_stats():
   db=connect_db()
   cursor= db.cursor()
   query=(""" Select Count(*) as total, sum(application_status = 'Applied' ) as applied,
          sum(application_status='Rejected') as rejected,
          sum(application_status='Accepted') as accepted 
          from applications""")
   cursor.execute(query)
   result = cursor.fetchone()
   cursor.close()
   db.close()
   return result
def search_applications(keyword):
   db = connect_db()
   cursor = db.cursor(dictionary=True)
   query = """ select * from applications 
   where company like  %s 
   or position like %s 
   order by id desc """
   like_pattern = f"%{keyword}%"
   cursor.execute(query,(like_pattern,like_pattern))
   result = cursor.fetchall()
   cursor.close()
   db.close()
   return result

def export_to_csv(filename="applications.csv"):
   conn = connect_db()
   cursor = conn.cursor()
   query="Select * from applications"
   cursor.execute(query)
   rows = cursor.fetchall()
   columns = [desc[0] for desc in cursor.description]
   with open(filename , mode="w",newline="",encoding="utf8") as file:
      writer = csv.writer(file)
      writer.writerow(columns)
      writer.writerows(rows)
   cursor.close()
   conn.close()
   print(f"{filename}, dosyası başarıyla oluşturuldu")
if False:
 add_application(
    company="Google",
    position="Data Analyst Intern",
    salary=1000,
    application_status="Applied",
    date_applied="2026-02-21",
    job_link="https://careers.google.com/job123",
    notes="Referral ile başvurdum"
)