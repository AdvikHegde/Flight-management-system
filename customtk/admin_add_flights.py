from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import customtkinter as ctk
import time

from admin_details import admin_details

import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='1234',database='flight_mgt_system')
my_cursor=conn.cursor()


def admin_add_flights():
  window=Toplevel()
  window.title("ADD FLIGHTS")
  window.geometry("1000x500")
  
  #FRAMES OF PAGE
  #FRAME0 ADMIN DASHBOARD
  frame0=Frame(window,width=150,height=500,bg="#ADD8E6",highlightbackground='black',highlightthickness=2)

  #HOME BUTTON
  home_btn=Button(frame0,text='HOME',font=("Times new Roman",15),bg='#E6BBAD',width=7,anchor="center",bd=0,highlightbackground='BLACK',highlightthickness=1  )
  home_btn.place(x=25,y=50)

  #MY DETAILS
  mydetails_btn=Button(frame0,text='MY DETAILS',font=("Times new Roman",10),bg='#E6BBAD',bd=0,highlightbackground='BLACK',highlightthickness=1,command=lambda:admin_details())
  mydetails_btn.place(x=25,y=375)
  
  #LOGOUT 
  logout_btn=Button(frame0,text='LOG OUT',font=("Times new Roman",10),bg='#E6BBAD',width=11,anchor="center",bd=0,highlightbackground='BLACK',highlightthickness=1,   command=lambda:logout())
  logout_btn.place(x=25,y=425)

  frame0.place(x=0,y=0) 

  #FRAME ON RIGHT SIDE OF PAGE
  frame1=Frame(window,width=850,height=500,bg="#FC9E4F")
  frame1.place(x=150,y=0)
  
  #FMS LOGO(CANNOT ADD FOR SOME REASON)

  
  img_f2=Image.open("customtk/newimages/whitebg.jpg")
  photo_f2=ImageTk.PhotoImage(img_f2)
  frame1_image_label=Label(frame1,image=photo_f2)
  frame1_image_label.place(x=0,y=0) 


  #LOGOUT CODE
  def logout():
      ans=messagebox.askquestion('LOGOUT',"Are you sure you want to logout?")
      if ans == 'yes':
          messagebox.showinfo('',"You have successfully logged out.")
          time.sleep(1)
          window.destroy()
      else:
          pass 
  
  
  #DESC OF THE PAGE 
  Font_tuple = ("Times new Roman", 20)
  frame1_text_Label1=Label(frame1,text="ADDING FLIGHTS",font=(Font_tuple),bg="WHITE",fg="#2D92B3")   
  frame1_text_Label1.place(relx=0.05,rely=0.025)
  
  frame1_text_Label2=Label(frame1,text="Please enter correct and verified details.",font=("Times new Roman",15),bg="WHITE")   
  frame1_text_Label2.place(relx=0.05,rely=0.10)
 
  

  #TEXT LABELS
  
  frame1_text_Label3=Label(frame1,text="Flight Details",font=("Times new Roman",12),bg="WHITE")   
  frame1_text_Label3.place(relx=0.05,rely=0.20)
  
  #FLIGHT NUMBER
  flight_number_label=Label(frame1,text="FLIGHT NUMBER:",bg="#FFFFFF",font=("bold",10))
  flight_number_entry=Entry(frame1,bg="#E6BBAD")
  
  flight_number_label.place(relx=0.05,rely=0.25)
  flight_number_entry.place(relx=0.225,rely=0.25)
  
  #FLIGHT NAME
  airline_label=Label(frame1,text="AIRLINE NAME:",bg="#FFFFFF",font=("bold",10))
  airline_label_combobox=ttk.Combobox(frame1,values=["Indigo","Vistara","Jet","Air India","Go Air"],width=15)

  airline_label.place(relx=0.45,rely=0.25)
  airline_label_combobox.place(relx=0.625,rely=0.25)
  
  
  frame1_text_Label4=Label(frame1,text="Source and Destination",font=("Times new Roman",12),bg="WHITE")   
  frame1_text_Label4.place(relx=0.05,rely=0.35)

  #SOURCE
  source_label=Label(frame1,text="SOURCE:",bg="#FFFFFF",font=("bold",10))
  source_entry=Entry(frame1,bg="#E6BBAD",width=20)
  source_label.place(relx=0.05,rely=0.40)
  source_entry.place(relx=0.225,rely=0.40)
  
  #DESTINATION
  destination_label=Label(frame1,text="DESTINATION:",bg="#FFFFFF",font=("bold",10))
  destination_entry=Entry(frame1,bg="#E6BBAD",width=20)
  destination_label.place(relx=0.45,rely=0.40)
  destination_entry.place(relx=0.625,rely=0.40)
  
  frame1_text_Label5=Label(frame1,text="Date and Time",font=("Times new Roman",12),bg="WHITE")   
  frame1_text_Label5.place(relx=0.05,rely=0.50)
  
  #DATE OF JOURNEY
  date_label=Label(frame1,text="DATE OF JOURNEY:",bg="#FFFFFF",font=("bold",10))
  date_entry=Entry(frame1,bg="#E6BBAD",width=20)
  date_label.place(relx=0.05,rely=0.55)
  date_entry.place(relx=0.225,rely=0.55)

  #TIME OF FLIGHT
  time_label=Label(frame1,text="TIME OF FLIGHT:",bg="#FFFFFF",font=("bold",10))
  time_entry=Entry(frame1,bg="#E6BBAD",width=20)
  time_label.place(relx=0.45,rely=0.55)
  time_entry.place(relx=0.625,rely=0.55)


  frame1_text_Label6=Label(frame1,text="Passenger capacity and Initial flight status",font=("Times new Roman",12),bg="WHITE")   
  frame1_text_Label6.place(relx=0.05,rely=0.65)

  #PASSENGER CAPACITY
  capacity_label=Label(frame1,text="CAPACITY:",bg="#FFFFFF",font=("bold",10))
  capacity_entry=Entry(frame1,bg="#E6BBAD",width=20)
  capacity_label.place(relx=0.05,rely=0.70)
  capacity_entry.place(relx=0.225,rely=0.70)


  #FLIGHT STATUS
  status_label=Label(frame1,text="FLIGHT STATUS:",bg="#FFFFFF",font=("bold",10))
  status_entry=Entry(frame1,bg="#E6BBAD",width=20)
  status_label.place(relx=0.45,rely=0.70)
  status_entry.place(relx=0.625,rely=0.70)

  #ADD FLIGHT BUTTON
  add_flight_button=Button(frame1,text="ADD FLIGHT",width=17,height=2,command=lambda:insert_data(),bg="#E6BBAD")
  add_flight_button.place(relx=0.625,rely=0.85)


  #DB CONNECTIVITY FOR ADD FLIGHTS
  def insert_data():
      flight_number=flight_number_entry.get()
      source=source_entry.get()
      destination=destination_entry.get()
      capacity=capacity_entry.get()
      airline=airline_label_combobox.get()
      date=date_entry.get()
      time=time_entry.get()
      status=status_entry.get()

      insert_query="INSERT INTO add_flights ('flight_number','source','destination','capacity','airline','date','time','status') VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
      vals=(flight_number,source,destination,capacity,airline,date,time,status)

      my_cursor.execute(insert_query,vals)
      conn.commit()

  window.mainloop()