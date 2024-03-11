from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import customtkinter as ctk
import time


from admin_details import admin_details


def admin_cancel_flights():
  window=Toplevel()
  window.title("CANCEL FLIGHTS")
  window.geometry("1000x500")

  
  def cancel_flight():
    ans=messagebox.askquestion('','Are you sure you want to cancel the flight?')
    if ans =='yes':
      messagebox.showinfo('','The flight has been cancelled.')
    else:
      pass
    
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
  frame1_text_Label1=Label(frame1,text="CANCELLING FLIGHTS",font=(Font_tuple),bg="WHITE",fg="#2D92B3")   
  frame1_text_Label1.place(relx=0.05,rely=0.025)
  
  frame1_text_Label2=Label(frame1,text="Please enter correct and verified details.",font=("Times new Roman",15),bg="WHITE")   
  frame1_text_Label2.place(relx=0.05,rely=0.10)
  
  
  #TEXT LABELS
  
  internal_frame1=LabelFrame(frame1,width=750,height=65,bg="#FFFFFF",bd=2,highlightbackground='BLACK',highlightthickness=1,text='Flight Number to generate details')
  internal_frame1.place(relx=0.05,rely=0.2)
  
  #FLIGHT NUMBER
  flight_number_label=Label(internal_frame1,text="FLIGHT NUMBER:",bg="#FFFFFF",font=("bold",10))
  flight_number_entry=Entry(internal_frame1,bg="#E6BBAD",width=20)
  flight_number_label.place(relx=0.05,rely=0.20)
  flight_number_entry.place(relx=0.225,rely=0.20)
  
  #GENERATE DETAILS
  generate_details_button=Button(internal_frame1,text="GENERATE DETAILS",font=("bold",10),height=2,width=30,bg="#E6BBAD")
  generate_details_button.place(relx=0.45,rely=0)

  

  internal_frame_2=LabelFrame(frame1,width=750,height=250,bg="#FFFFFF",bd=2,highlightbackground='BLACK',highlightthickness=1,text='FLIGHT DETAILS')
  internal_frame_2.place(relx=0.05,rely=0.35)
  
  #FLIGHT NAME
  airline_label=Label(internal_frame_2,text="AIRLINE NAME:",bg="#FFFFFF",font=("bold",10))
  airline_label_entry=Entry(internal_frame_2,bg="#E6BBAD",width=20)

  airline_label.place(relx=0.05,rely=0.10)
  airline_label_entry.place(relx=0.225,rely=0.10)
  
  #PASSENGER CAPACITY
  passenger_label=Label(internal_frame_2,text="CAPACITY:",bg="#FFFFFF",font=("bold",10))
  passenger_entry=Entry(internal_frame_2,bg="#E6BBAD",width=20)
  passenger_label.place(relx=0.45,rely=0.10)
  passenger_entry.place(relx=0.625,rely=0.10)
  
  #SOURCE
  source_label=Label(internal_frame_2,text="SOURCE:",bg="#FFFFFF",font=("bold",10))
  source_entry=Entry(internal_frame_2,bg="#E6BBAD",width=20)
  source_label.place(relx=0.05,rely=0.3)
  source_entry.place(relx=0.225,rely=0.3)

  #DESTINATION
  destination_label=Label(internal_frame_2,text="DESTINATION:",bg="#FFFFFF",font=("bold",10))
  destination_entry=Entry(internal_frame_2,bg="#E6BBAD",width=20)
  destination_label.place(relx=0.45,rely=0.3)
  destination_entry.place(relx=0.625,rely=0.3)

  #DATE OF JOURNEY
  date_label=Label(internal_frame_2,text="DATE OF JOURNEY:",bg="#FFFFFF",font=("bold",10))
  date_entry=Entry(internal_frame_2,bg="#E6BBAD",width=20)
  date_label.place(relx=0.05,rely=0.50)
  date_entry.place(relx=0.225,rely=0.50)

  #TIME OF FLIGHT
  time_label=Label(internal_frame_2,text="TIME OF FLIGHT:",bg="#FFFFFF",font=("bold",10))
  time_entry=Entry(internal_frame_2,bg="#E6BBAD",width=20)
  time_label.place(relx=0.45,rely=0.50)
  time_entry.place(relx=0.625,rely=0.50)

  #FLIGHT STATUS
  status_label=Label(internal_frame_2,text="FLIGHT STATUS:",bg="#FFFFFF",font=("bold",10))
  status_entry=ttk.Combobox(internal_frame_2,values=["Delayed","Cancelled","On Time"],width=17)
  status_label.place(relx=0.05,rely=0.70)
  status_entry.place(relx=0.225,rely=0.70)

  
  
  cancel_flight_button=Button(frame1,text="CANCEL FLIGHT",command=lambda:cancel_flight(),width=20,height=2,bg="#E6BBAD")
  cancel_flight_button.place(relx=0.755,rely=0.90)
  
  
  window.mainloop()
