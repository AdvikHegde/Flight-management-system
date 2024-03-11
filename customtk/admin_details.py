from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk


import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='1234',database='flight_mgt_system')
my_cursor=conn.cursor()



def admin_details():
  window=Tk()
  window.title("ADMIN DETAILS")
  window.geometry("1000x500")
  window.minsize(1000,500)



  frame1=Frame(window,width=500,height=500,bg="#FC9E4F")
  frame1.place(x=500,y=0)

  #CREATING AND PLACING WIDGETS FOR LOGIN PAGE
  login_label=Label(frame1,text="MY DETAILS",font=("Times new roman",15),bg="#FF521B")

  admin_id_label=Label(frame1,text="ADMIN ID:",bg="#FF521B",font=("bold",10),width=10)
  admin_id_entry=Entry(frame1,bg="#EDD382")

  password_label=Label(frame1,text="PASSWORD:",bg="#FF521B",font=("bold",10))
  password_entry=Entry(frame1,bg="#EDD382")

  admin_code_label=Label(frame1,text="ADMIN CODE:",bg="#FF521B",font=("bold",10))
  admin_code_entry=Entry(frame1,bg="#EDD382")

  reset_details_button=Button(frame1,text="RESET DETAILS",command=lambda:insert_data())



  #PLACING THE LABELS AND ENTRIES
  login_label.place(relx=0.5, rely=0.10, anchor="n")

  admin_id_label.place(relx=0.025,rely=0.25)
  admin_id_entry.place(relx=0.225,rely=0.25)

  password_label.place(relx=0.5,rely=0.25)
  password_entry.place(relx=0.70,rely=0.25)

  admin_code_label.place(relx=0.025,rely=0.35)
  admin_code_entry.place(relx=0.2255,rely=0.35)

  reset_details_button.place(relx=0.70,rely=0.55,relheight=0.1,relwidth=0.25)
  
  def insert_data():
    adminid=admin_id_entry.get()
    admincode=admin_code_entry.get()
    pwd=password_entry.get()

    
    insert_query="INSERT INTO admin_details (admin_id,admin_code,pwd) VALUES (%s,%s,%s)"
    vals=(adminid,admincode,pwd)
    
    my_cursor.execute(insert_query,vals)
    conn.commit()

  window.mainloop()
admin_details()