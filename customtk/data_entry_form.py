from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import customtkinter as ctk
import time

def admin_passenger_info():
  window=Tk()
  window.title("DATA ENTRY PAGE")
  window.geometry("1000x500")

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
  passenger_info_frame=LabelFrame(parent_frame,bg="#FC9E4F",text="PASSENGER CUSTOMER ID")
  passenger_info_frame.grid(row=0,column=1 ,columnspan=2,padx=20,pady=10)

  #TEXT LABELS
  
  def view_info():
    pass

  #CUSTOMER ID
  passenger_customerid_label=Label(passenger_info_frame,text="CUSTOMER ID:",bg="#FF521B",font=("bold",10),width=15)
  passenger_customerid_entry=Entry(passenger_info_frame,bg="#EDD382",width=20)
  passenger_customerid_label.grid(column=1,row=1,padx=20,pady=10)
  passenger_customerid_entry.grid(column=2,row=1,padx=20,pady=10)
  
  view_info_button=Button(passenger_info_frame,text="SEARCH",command=lambda:view_info(),width=15,height=2)
  view_info_button.grid(column=3,row=1,padx=20,pady=10)
  
  
  
  
  passenger_info_frame=LabelFrame(parent_frame,bg="#FC9E4F",text="PASSENGER INFORMATION")
  passenger_info_frame.grid(row=2,column=1 ,columnspan=2,padx=20,pady=10)
  #NAME
  passenfer_name_label=Label(passenger_info_frame,text="NAME:",bg="#FF521B",font=("bold",10),width=15)
  passenfer_name_entry=Entry(passenger_info_frame,bg="#EDD382",width=20)
  passenfer_name_label.grid(column=1,row=3,padx=20,pady=10)
  passenfer_name_entry.grid(column=1,row=4,padx=20,pady=20)
  
  #AGE
  passenger_age_label=Label(passenger_info_frame,text="AGE:",bg="#FF521B",font=("bold",10),width=15)
  passenger_age_entry=Entry(passenger_info_frame,bg="#EDD382",width=20)
  passenger_age_label.grid(column=2,row=3,padx=20,pady=10)
  passenger_age_entry.grid(column=2,row=4,padx=20,pady=20)
  
  #PHONE NUMBER
  passenger_contactnum_label=Label(passenger_info_frame,text="PHONE NUMBER:",bg="#FF521B",font=("bold",10),width=15)
  passenger_contactnum_entry=Entry(passenger_info_frame,bg="#EDD382",width=20)
  passenger_contactnum_label.grid(column=3,row=3,padx=20,pady=10)
  passenger_contactnum_entry.grid(column=3,row=4,padx=20,pady=20)
  
  #ADDRESS
  passenger_address_label=Label(passenger_info_frame,text="ADDRESS:",bg="#FF521B",font=("bold",10),width=15)
  passenger_address_entry=Entry(passenger_info_frame,bg="#EDD382",width=20)
  passenger_address_label.grid(column=1,row=5,padx=20,pady=10)
  passenger_address_entry.grid(column=1,row=6,padx=20,pady=10)
  
  #EMAILID
  passenger_email_label=Label(passenger_info_frame,text="EMAIL:",bg="#FF521B",font=("bold",10),width=15)
  passenger_email_entry=Entry(passenger_info_frame,bg="#EDD382",width=20)
  passenger_email_label.grid(column=2,row=5,padx=20,pady=10)
  passenger_email_entry.grid(column=2,row=6,padx=20,pady=10)
  
  #CURRENT BOOKINGS OF CUSTOMER
  passenger_customerid_label=Label(passenger_info_frame,text="CUSTOMER ID:",bg="#FF521B",font=("bold",10),width=15)
  passenger_customerid_entry=Entry(passenger_info_frame,bg="#EDD382",width=20)
  passenger_customerid_label.grid(column=3,row=5,pady=10)
  passenger_customerid_entry.grid(column=3,row=6,pady=10)
  
  view_info_button=Button(parent_frame,text="SEARCH FLIGHTS",command=lambda:view_info(),width=15,height=2)
  view_info_button.grid(column=2,row=7,padx=20,pady=20,columnspan=2,sticky='news')
  
  window.mainloop()