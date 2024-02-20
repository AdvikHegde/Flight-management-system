from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import customtkinter as ctk
import time

from admin_details import admin_details
from admin_add_flights import admin_add_flights
from admin_cancel_flights import admin_cancel_flights
from admin_update_flights import admin_update_flights
from admin_passenger_info import admin_passenger_info


def admin_page():
    window=Tk()
    window.title("ADMIN PAGE")
    window.geometry("1000x500")   
    
    #FRAME ON LEFT SIDE OF PAGE
    frame1=Frame(window,width=300,height=500,bg="#FC9E4F")
    frame1.place(x=0,y=0)

    #FRAME ON RIGHT SIDE OF PAGE
    frame2=Frame(window,width=700,height=500,bg="#FC9E4F")
    frame2.place(x=300,y=0)  

      
    img_f2=Image.open("customtk/Images/5.jpg")
    photo_f2=ImageTk.PhotoImage(img_f2)
    frame2_image_label=Label(frame2,image=photo_f2)
    frame2_image_label.place(x=0,y=0) 
    
    
    Font_tuple = ("Times new Roman", 20)
    frame2_text_Label=Label(frame2,text="ADMIN FUNCTIONS",font=(Font_tuple),bg="#ab23ff")   
    frame2_text_Label.place(relx=0.35,rely=0.035)
    
    #ADMIN MENU FRAME ITEMS
    #MY DETAILS
    img01=Image.open("customtk/Images/9.png")
    photo01=ImageTk.PhotoImage(img01)
    
    my_details_button = Button(frame1,image=photo01,command=lambda:admin_details())
    my_details_button.place(relx=0.35,rely=0.15)
    
    my_details_label=Label(frame1,text="MY DETAILS")
    my_details_label.place(relx=0.40,rely=0.375)

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
    
    signout_button = Button(frame1,image=photo02,command=lambda:logout())
    signout_button.place(relx=0.35,rely=0.6)
    
    signout_Label=Label(frame1,text="LOG OUT")   
    signout_Label.place(relx=0.45,rely=0.825)
    
    
    #ADDING IMAGEICONS TO ADMIN FUNCTIONALITIES 
    #ADD FLIGHTS
    img1=Image.open("customtk/Images/1.jpg")
    photo1=ImageTk.PhotoImage(img1)
    
    add_flights_button=Button(frame2,image=photo1,bg="#FF521B",font=("bold",10),command=lambda:admin_add_flights())
    add_flights_button.place(relx=0.14,rely=0.15)
    
    add_flights_text_label=Label(frame2,text="ADD FLIGHTS",font=("bold",10),bg="#FF521B")
    add_flights_text_label.place(relx=0.150,rely=0.375)
    

    
    #CANCEL FLIGHTS
    img2=Image.open("customtk/Images/6.jpg")
    photo2=ImageTk.PhotoImage(img2)
    
    cancel_flights_button=Button(frame2,image=photo2,bg="#FF521B",font=("bold",10),command=lambda:admin_cancel_flights())
    cancel_flights_button.place(relx=0.765,rely=0.15)
    
    cancel_flights_label=Label(frame2,text="CANCEL FLIGHTS",bg="#FF521B",font=("bold",10),width=15)
    cancel_flights_label.place(relx=0.75,rely=0.375)
    
    
    #UPDATE FLIGHTS
    img3=Image.open("customtk/Images/7.png")
    photo3=ImageTk.PhotoImage(img3)
    
    update_flights_button=Button(frame2,image=photo3,font=("bold",10),command=lambda:admin_update_flights())
    update_flights_button.place(relx=0.14,rely=0.600)
    
    update_flights_label=Label(frame2,text="UPDATE FLIGHTS",bg="#FF521B",font=("bold",10),width=15)
    update_flights_label.place(relx=0.127,rely=0.825)
    
    
    #PASSENGER INFO
    img4=Image.open("customtk/Images/8.jpg")
    photo4=ImageTk.PhotoImage(img4)
    
    passenger_info_button=Button(frame2,image = photo4,font=("bold",10),command=lambda:admin_passenger_info())
    passenger_info_button.place(relx=0.765,rely=0.600)
    
    view_passenger_info_label=Label(frame2,text="PASSENGER INFO",bg="#FF521B",font=("bold",10),width=15)
    view_passenger_info_label.place(relx=0.75,rely=0.825)
    
    window.mainloop()
    
admin_page()