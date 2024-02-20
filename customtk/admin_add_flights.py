from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import customtkinter as ctk
import time

from admin_details import admin_details


def admin_add_flights():
  window=Toplevel()
  window.title("L PAGE")

  #FRAME ON   COMPLETE PAGE
  parent_frame=Frame(window,bg="#FC9E4F")
  parent_frame.pack()
  
  #FRAME ON LEFT SIDE OF PAGE
  dashboard_frame=LabelFrame(parent_frame,text="DASHBOARD",bg="#FC9E4F")
  dashboard_frame.grid(row=0,column=0,rowspan=8,padx=20,pady=10,sticky='news')
  
  #MY DETAILS
  img01=Image.open("customtk/Images/9.png")
  photo01=ImageTk.PhotoImage(img01)
  
  my_details_button = Button(dashboard_frame,image=photo01,command=lambda:admin_details())
  my_details_button.grid(row=1,column=0,pady=10)
  
  my_details_label=Label(dashboard_frame,text="MY DETAILS",bg="#FF521B")
  my_details_label.grid(row=2,column=0)
  

  #LOGOUT
  def logout():
      ans=messagebox.askquestion('LOGOUT',"Are you sure you want to logout?")
      if ans == 'yes':
          messagebox.showinfo('',"You have successfully logged out.")
          time.sleep(1)
          window.destroy()
      else:
          pass 
  
  img02=Image.open("customtk/Images/10.jpg")
  photo02=ImageTk.PhotoImage(img02)
  
  signout_button = Button(dashboard_frame,image=photo02,command=lambda:logout())
  signout_button.grid(row=3,column=0,pady=10)
  
  signout_Label=Label(dashboard_frame,text="LOG OUT",bg="#FF521B")   
  signout_Label.grid(row=4,column=0)
  

  #FRAME ON RIGHT SIDE OF PAGE
  flight_info_frame=LabelFrame(parent_frame,bg="#FC9E4F",text="FLIGHT INFORMATION")
  flight_info_frame.grid(row=0,column=1 ,columnspan=2,padx=20,pady=10)

  #TEXT LABELS
  #FLIGHT NUMBER
  flight_number_label=Label(flight_info_frame,text="FLIGHT NUMBER:",bg="#FF521B",font=("bold",10),width=15)
  flight_number_entry=Entry(flight_info_frame,bg="#EDD382",width=20)
  flight_number_label.grid(row=0,column=1,padx=20,pady=5)
  flight_number_entry.grid(row=1,column=1,padx=20,pady=5)

  #SOURCE
  source_label=Label(flight_info_frame,text="SOURCE:",bg="#FF521B",font=("bold",10),width=15)
  source_entry=Entry(flight_info_frame,bg="#EDD382",width=20)
  source_label.grid(row=0,column=2,padx=20,pady=5)
  source_entry.grid(row=1,column=2,padx=20,pady=5)

  #FLIGHT NAME
  airline_label=Label(flight_info_frame,text="AIRLINE NAME:",bg="#FF521B",font=("bold",10),width=15)
  airline_label_combobox=ttk.Combobox(flight_info_frame,values=["Indigo","Vistara","Jet","Air India","Go Air"],width=15)

  airline_label.grid(row=0,column=3,padx=20,pady=5)
  airline_label_combobox.grid(row=1,column=3,padx=20,pady=5)
  
  #PASSENGER CAPACITY
  passenger_label=Label(flight_info_frame,text="CAPACITY:",bg="#FF521B",font=("bold",10),width=15)
  passenger_entry=Entry(flight_info_frame,bg="#EDD382",width=20)
  passenger_label.grid(row=2,column=1,padx=20,pady=5)
  passenger_entry.grid(row=3,column=1,padx=20,pady=5)

  #DESTINATION
  destination_label=Label(flight_info_frame,text="DESTINATION:",bg="#FF521B",font=("bold",10),width=15)
  destination_entry=Entry(flight_info_frame,bg="#EDD382",width=20)
  destination_label.grid(row=2,column=2,padx=20,pady=5)
  destination_entry.grid(row=3,column=2,padx=20,pady=5)




  #FRAME DISPLAYING DATE AND TIME WIDGETS
  datetime_info_frame=LabelFrame(parent_frame,bg="#FC9E4F",text="DATE AND TIME")
  datetime_info_frame.grid(row=4,column=1 ,columnspan=2,padx=20,pady=20,sticky='news')

  #DATE OF JOURNEY
  date_label=Label(datetime_info_frame,text="DATE OF JOURNEY:",bg="#FF521B",font=("bold",10),width=15)
  date_entry=Entry(datetime_info_frame,bg="#EDD382",width=20)
  date_label.grid(row=5,column=1,padx=20,pady=5)
  date_entry.grid(row=6,column=1,padx=20,pady=5)

  #TIME OF FLIGHT
  time_label=Label(datetime_info_frame,text="TIME OF FLIGHT:",bg="#FF521B",font=("bold",10),width=15)
  time_entry=Entry(datetime_info_frame,bg="#EDD382",width=20)
  time_label.grid(row=5,column=2,padx=20,pady=5)
  time_entry.grid(row=6,column=2,padx=20,pady=5)



  #FRAME DISPLAYING RUNNING STATUS
  runningstatus_info_frame=LabelFrame(parent_frame,bg="#FC9E4F",text="RUNNING STATUS")
  runningstatus_info_frame.grid(row=7,column=1,columnspan=2,padx=20,pady=20,sticky='news')

  #FLIGHT STATUS
  status_label=Label(runningstatus_info_frame,text="FLIGHT STATUS:",bg="#FF521B",font=("bold",10),width=15)
  status_entry=Entry(runningstatus_info_frame,bg="#EDD382",width=20)
  status_label.grid(row=8,column=1,padx=20,pady=5)
  status_entry.grid(row=9,column=1,padx=20,pady=5)

  #ADD FLIGHT BUTTON
  add_flight_button=Button(parent_frame,text="ADD FLIGHT",width=17,height=2)
  add_flight_button.grid(row=9,column=2,padx=20,pady=10,sticky='news')

  window.mainloop()