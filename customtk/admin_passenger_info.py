from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import customtkinter as ctk
import time

from admin_details import admin_details

def admin_passenger_info():
  window=Toplevel()
  window.title("DATA ENTRY PAGE")
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
  frame1_text_Label1=Label(frame1,text="PASSENGER INFORMATION",font=(Font_tuple),bg="WHITE",fg="#2D92B3")   
  frame1_text_Label1.place(relx=0.05,rely=0.025)
  
  frame1_text_Label2=Label(frame1,text="Please enter correct and verified details.",font=("Times new Roman",15),bg="WHITE")   
  frame1_text_Label2.place(relx=0.05,rely=0.10)


  
  def view_info():
    pass

  #TEXT LABELS 
  #INTERNAL FRAME 1
  internal_frame_1=LabelFrame(frame1,width=750,height=65,bg="#FFFFFF",bd=2,highlightbackground='BLACK',highlightthickness=1,text='Customer ID to generate details')
  internal_frame_1.place(relx=0.05,rely=0.2)

  #CUSTOMER ID
  passenger_customerid_label=Label(internal_frame_1,text="CUSTOMER ID:",bg="#FFFFFF",font=("bold",10))
  passenger_customerid_entry=Entry(internal_frame_1,bg="#E6BBAD",width=20)
  passenger_customerid_label.place(relx=0.05,rely=0.2)
  passenger_customerid_entry.place(relx=0.225,rely=0.2)
  
  view_info_button=Button(internal_frame_1,text="SEARCH",command=lambda:view_info(),height=1,bg="#E6BBAD",width=20)
  view_info_button.place(relx=0.625,rely=0.15)
  
  
  #INTERNAL FRAME 2
  internal_frame_2=LabelFrame(frame1,width=750,height=250,bg="#FFFFFF",bd=2,highlightbackground='BLACK',highlightthickness=1,text='Passenger Information')
  internal_frame_2.place(relx=0.05,rely=0.35)
  

  #NAME
  passenger_name_label=Label(internal_frame_2,text="NAME:",bg="#FFFFFF",font=("bold",10))
  passenger_name_entry=Entry(internal_frame_2,bg="#E6BBAD",width=20)
  passenger_name_label.place(relx=0.05,rely=0.10)
  passenger_name_entry.place(relx=0.225,rely=0.10)
  
  #AGE
  passenger_age_label=Label(internal_frame_2,text="AGE:",bg="#FFFFFF",font=("bold",10))
  passenger_age_entry=Entry(internal_frame_2,bg="#E6BBAD",width=20)
  passenger_age_label.place(relx=0.45,rely=0.10)
  passenger_age_entry.place(relx=0.625,rely=0.10)
  
  #PHONE NUMBER
  passenger_contactnum_label=Label(internal_frame_2,text="PHONE NUMBER:",bg="#FFFFFF",font=("bold",10))
  passenger_contactnum_entry=Entry(internal_frame_2,bg="#E6BBAD",width=20)
  passenger_contactnum_label.place(relx=0.05,rely=0.30)
  passenger_contactnum_entry.place(relx=0.225,rely=0.30)
  
  #ADDRESS
  passenger_address_label=Label(internal_frame_2,text="ADDRESS:",bg="#FFFFFF",font=("bold",10))
  passenger_address_entry=Entry(internal_frame_2,bg="#E6BBAD",width=20)
  passenger_address_label.place(relx=0.45,rely=0.30)
  passenger_address_entry.place(relx=0.625,rely=0.30)
  
  #EMAILID
  passenger_email_label=Label(internal_frame_2,text="EMAIL:",bg="#FFFFFF",font=("bold",10))
  passenger_email_entry=Entry(internal_frame_2,bg="#E6BBAD",width=20)
  passenger_email_label.place(relx=0.05,rely=0.50)
  passenger_email_entry.place(relx=0.225,rely=0.50)
  
  #CURRENT BOOKINGS OF CUSTOMER
  passenger_ticket_desc=Message(internal_frame_2,text="Details about ticket of passenger based on ID ticket,coach,seat number,cost,date of flight and any other relevant information.",font=("Helvetica",10),width=800,bd=1,highlightbackground='BLACK',highlightthickness=1)
  passenger_ticket_desc.place(relx=0.005,rely=0.80)

  #PREFERABLY SHOULD USE A MESSAGE BOX TO DISPLAY ALL THE REQUIRED INFORMATION ABOUT TICKET AND BOOKING DETAILS OF THE PASSENGER IN A SINGLE DISPLAY MESSAGE
  
  view_info_button=Button(frame1,text="VIEW INFO",command=lambda:view_info(),height=2,bg="#E6BBAD",width=20)
  view_info_button.place(relx=0.760,rely=0.875)
  
  window.mainloop()