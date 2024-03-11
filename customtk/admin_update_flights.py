from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import customtkinter as ctk
import time

from admin_details import admin_details

def admin_update_flights():
  window=Toplevel()
  window.title("UPDATE FLIGHTS PAGE")
  window.geometry("1000x500")
  
  def update_flight():
    ans=messagebox.askquestion('','Are you sure you want to update the flight details?')
    if ans =='yes':
      messagebox.showinfo('','The flight details have been updated.')
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
  frame1_text_Label1=Label(frame1,text="UPDATE FLIGHT DETAILS",font=(Font_tuple),bg="WHITE",fg="#2D92B3")   
  frame1_text_Label1.place(relx=0.05,rely=0.025)
  
  frame1_text_Label2=Label(frame1,text="Please enter correct and verified details.",font=("Times new Roman",15),bg="WHITE")   
  frame1_text_Label2.place(relx=0.05,rely=0.10)  
  
  #TEXT LABELS
  
  #INTERNAL FRAME 1
  internal_frame_1=LabelFrame(frame1,width=750,height=200,bg="#FFFFFF",bd=2,highlightbackground='BLACK',highlightthickness=1,text='Flight Details')
  internal_frame_1.place(relx=0.05,rely=0.2)

  #FLIGHT NUMBER
  flight_number_label=Label(internal_frame_1,text="FLIGHT NUMBER:",bg="#FFFFFF",font=("bold",10),)
  flight_number_entry=Entry(internal_frame_1,bg="#E6BBAD",width=20)
  flight_number_label.place(relx=0.05,rely=0.25)
  flight_number_entry.place(relx=0.30,rely=0.25)
  
  #FLIGHT STATUS
  status_label=Label(internal_frame_1,text="NEW FLIGHT STATUS:",bg="#FFFFFF",font=("bold",10))
  status_entry_combobox=ttk.Combobox(internal_frame_1,width=20,values=["Delayed","Cancelled"])
  status_label.place(relx=0.5,rely=0.25)
  status_entry_combobox.place(relx=0.70,rely=0.25)
  
  
  #TIME OF FLIGHT
  time_label=Label(internal_frame_1,text="UPDATED TIME OF FLIGHT:",bg="#FFFFFF",font=("bold",10))
  time_entry=Entry(internal_frame_1,bg="#E6BBAD",width=20)
  time_label.place(relx=0.05,rely=0.5)
  time_entry.place(relx=0.30,rely=0.5)
  
  #REASON FOR DELAY
  status_label=Label(internal_frame_1,text="REASON FOR DELAY:",bg="#FFFFFF",font=("bold",10))
  status_entry_combobox=ttk.Combobox(internal_frame_1,width=17,values=["Weather","Maintenance","Operations Delay","Security"])
  status_label.place(relx=0.05,rely=0.75)
  status_entry_combobox.place(relx=0.30,rely=0.75)
  
  
  generate_update_message_button=Button(internal_frame_1,text="GENERATE UPDATE MESSAGE",width=25,height=2,bg="#E6BBAD")
  generate_update_message_button.place(relx=0.70,rely=0.65)

  #INTERNAL FRAME 2
  internal_frame_2=LabelFrame(frame1,width=750,height=100,bg="#FFFFFF",bd=2,highlightbackground='BLACK',highlightthickness=1,text='Update message')
  internal_frame_2.place(relx=0.05,rely=0.75)
  
  #SEND UPDATE MESSAGE
  update_message_entry=Entry(internal_frame_2,bg="#E6BBAD",width=15,font=('Arial 30'))
  update_message_entry.place(relx=0.05,rely=0.25)
  
  send_update_message_button=Button(internal_frame_2,text="SEND UPDATE MESSAGE",width=25,height=2,command=lambda:update_flight(),bg="#E6BBAD")
  send_update_message_button.place(relx=0.70,rely=0.25)
  
  
  window.mainloop()
  