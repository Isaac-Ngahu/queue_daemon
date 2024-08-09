import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()
port = os.getenv('MYSQLPORT', '3306')
mydb = mysql.connector.connect(
  host=os.getenv('MYSQLHOST'),
  user=os.getenv('MYSQLUSER'),
  database=os.getenv('MYSQLDATABASE'),
  port=int(port),
  password=os.getenv('MYSQLPASSWORD')
)

def insert_message_details(message,destination,origin):
    sql = "INSERT INTO sms_table (message,destination,origin) VALUES(%s,%s,%s)"
    values = (message,destination,origin)
    mycursor = mydb.cursor()
    try:
        mycursor.execute(sql,values)
        mydb.commit()
        return "inserted"
    finally:
        mycursor.close()

def fetch_messages():
  sql = "SELECT * FROM sms_table LIMIT 10"
  mycursor = mydb.cursor()
  try:
    mycursor.execute(sql)
    messages = mycursor.fetchall()
    mydb.commit()
    return messages
  except Exception as e:
     print(e)
  finally:
     mycursor.close()

def delete_message(id):
  sql = "DELETE FROM sms_table WHERE id=%s"
  values = (id,)
  mycursor = mydb.cursor()
  try:
    mycursor.execute(sql,values)
    mydb.commit()
    return "deleted"
  except Exception as e:
    print(e)
  finally:
    mycursor.close()

def insert_into_sms_archive(message):
  sql = "INSERT INTO sms_archive (message,destination,origin) VALUES(%s,%s,%s)"
  values = (message[1],message[2],message[3])
  mycursor = mydb.cursor()
  try:
    mycursor.execute(sql,values)
    mydb.commit()
    return "inserted"
  except Exception as e:
    print(e)
  finally:
    mycursor.close()


# print(fetch_messages())
# print(int("254705832092"))
print(type(os.getenv('MYSQLPORT')))