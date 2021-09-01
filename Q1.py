import mysql.connector as connection
import pandas as pd
try:
    mydb = connection.connect(host=input("hostname:"), database = input("databse-name:"),user=input("user-name:"), passwd=input("password:"),use_pure=True)
    user_input = input("Which table do you want to see?:")

    # provide any table you have in your database.
    query = f"Select * from {user_input};" 
    result_dataFrame = pd.read_sql(query,mydb)
    print(result_dataFrame)
    mydb.close() 
    
except Exception as e:
    mydb.close()
    print(str(e))