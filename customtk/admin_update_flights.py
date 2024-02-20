from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import customtkinter as ctk
import time

from admin_details import admin_details

def admin_update_flights():
  window=Toplevel()
  window.title("UPDATE FLIGHTS PAGE")
  
  def update_flight():
    ans=messagebox.askquestion('','Are you sure you want to update the flight details?')
    if ans =='yes':
      messagebox.showinfo('','The flight details have been updated.')
    else:
      pass
    
    
  #FRAME ON RIGHT SIDE OF PAGE
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
  flight_info_frame.grid(row=0,column=2 ,columnspan=2,padx=20,pady=10)
    
  #TEXT LABELS
  #FLIGHT NUMBER
  flight_number_label=Label(parent_frame,text="FLIGHT NUMBER:",bg="#FF521B",font=("bold",10),width=20)
  flight_number_entry=Entry(parent_frame,bg="#EDD382",width=20)
  flight_number_label.grid(row=0,column=1,padx=20,pady=10)
  flight_number_entry.grid(row=1,column=1,padx=20,pady=10,sticky='news')
  
  #FLIGHT STATUS
  status_label=Label(parent_frame,text="NEW FLIGHT STATUS:",bg="#FF521B",font=("bold",10),width=20)
  status_entry_combobox=ttk.Combobox(parent_frame,width=20,values=["Delayed","Cancelled"])
  status_label.grid(row=0,column=2,padx=20,pady=10)
  status_entry_combobox.grid(row=1,column=2,padx=20,pady=10,sticky='news')
  
  
  #TIME OF FLIGHT
  time_label=Label(parent_frame,text="UPDATED TIME OF FLIGHT:",bg="#FF521B",font=("bold",10),width=20)
  time_entry=Entry(parent_frame,bg="#EDD382",width=20)
  time_label.grid(row=2,column=1,padx=20,pady=10)
  time_entry.grid(row=3,column=1,padx=20,pady=10,sticky='news')
  
  generate_update_message_button=Button(parent_frame,text="GENERATE UPDATE MESSAGE",width=22,height=2)
  generate_update_message_button.grid(column=2,row=2,rowspan=2)
  
  
  #UPDATE MESSAGE FRAME
  update_message_frame=LabelFrame(parent_frame,bg="#FC9E4F",text="UPDATE MESSAGE")
  update_message_frame.grid(row=4,column=1,columnspan=2,padx=20,pady=10)
  
  #GENERATE UPDATE MESSAGE
  update_message_entry=Entry(update_message_frame,bg="#EDD382",width=15,font=('Arial 30'))
  update_message_entry.grid(row=5,column=1,padx=20,pady=10,sticky='news')
  
  send_update_message_button=Button(parent_frame,text="SEND UPDATE MESSAGE",width=22,height=2,command=lambda:update_flight())
  send_update_message_button.grid(row=6,column=2,padx=20,pady=10)
  
  
  window.mainloop()
  