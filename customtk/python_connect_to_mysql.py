from admin_details import admin_details
from admin_add_flights import admin_add_flights
from admin_cancel_flights import admin_cancel_flights
from admin_update_flights import admin_update_flights
from admin_passenger_info import admin_passenger_info


import mysql.connector

conn=mysql.connector.connect(host='localhost',username='root',password='1234',database='flight_mgt_system')
my_cursor=conn.cursor()

if conn.is_connected():
  print("Connection established.")
  

my_cursor.execute()
conn.commit()
conn.close()
