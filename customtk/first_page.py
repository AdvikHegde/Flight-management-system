from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk

from admin_page import admin_page

window=Tk()
window.title("FIRST PAGE")
window.geometry("1000x500")
window.minsize(1000,500)

#2 FRAMES IN THIS PAGE
menu_frame=Frame(window)
main_frame=Frame(window,bg="#FC9E4F")

text_box=Text(main_frame,bg="#FF521B",font=("Times New Roman",15))
text_box.insert(INSERT,"Welcome to the \t \033FLIGHT MANAGEMENT SYSTEM.\033 \nWe hope your experience with this software is a comfortable one.")

text_label=Label(main_frame,text='ADMIN OR CUSTOMER',font=("Times new Roman",18,"bold"),bg="#FC9E4F")
admin_button=Button(main_frame,text="ADMIN")
customer_button=Button(main_frame,text="CUSTOMER")

#POSITIONING THE FRAMES
menu_frame.place(x=0,y=0,relwidth=0.4,relheight=1)
main_frame.place(relx=0.4,y=0,relwidth=0.6,relheight=1)

text_box.place(relx=0.05,rely=0.05,relwidth=0.90,relheight=0.10)
text_label.place(relx=0.05,rely=0.20,relwidth=0.90,relheight=0.10)

admin_button.place(relx=0.20,rely=0.35,relwidth=0.15,relheight=0.10)
customer_button.place(relx=0.65,rely=0.35,relwidth=0.15,relheight=0.10)


#MENU WIDGETS


frame1=Frame(window,width=500,height=500,bg="#FC9E4F")
frame1.place(x=500,y=0)

def login():
  if (username_entry.get()=="ADVIK" and password_entry.get()=="1234"):
    messagebox.showinfo("ALERT","LOGIN SUCCESSFUL.")
    
  else:
    messagebox.showinfo("ALERT","LOGIN UNSUCCESSFUL.")
    
 

#CREATING AND PLACING WIDGETS FOR LOGIN PAGE
login_label=Label(frame1,text="LOGIN PAGE",font=("Times new roman",15),bg="#FF521B")
username_label=Label(frame1,text="USERNAME:",bg="#FF521B",font=("bold",10))
username_entry=Entry(frame1,bg="#EDD382")
password_label=Label(frame1,text="PASSWORD:",bg="#FF521B",font=("bold",10))
password_entry=Entry(frame1,bg="#EDD382")
login_button=Button(frame1,text="LOGIN",command=login,bg="#FF521B",width=16)
welcome_message_label=Label(text="Welcome User,Please Enter your Deatils to Log In to the System.",font=("Times new roman",15),bg="#FF521B")

login_label.place(relx=0.5, rely=0.10, anchor="n")
username_label.place(relx=0.25,rely=0.25)
username_entry.place(relx=0.5,rely=0.25)
password_label.place(relx=0.25,rely=0.35)
password_entry.place(relx=0.5,rely=0.35)
login_button.place(relx=0.5,rely=0.45)


# Create a label to display the image
frame2=Frame(window,width=500,height=500,bg="#FFFFFF")
frame2.pack()
frame2.place(x=0,y=0)

img=Image.open("customtk/Images/img.jpg")
photo=ImageTk.PhotoImage(img)


# Create a Label Widget to display the text or Image
label = Label(frame2, image = photo,width=500,height=500,bg="#FFFFFF")
label.place(x=0,y=0)


window.mainloop()
