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

    #FRAMES OF PAGE
    #FRAME0 ADMIN DASHBOARD
    frame0=Frame(window,width=150,height=500,bg="#ADD8E6",highlightbackground='black',highlightthickness=2)
    
    home_btn=Button(frame0,text='HOME',font=("Times new Roman",15),bg='#E6BBAD',width=7,anchor="center",bd=0,highlightbackground='BLACK',highlightthickness=1  )
    home_btn.place(x=25,y=50)
    
    # home_logo = Image.open("customtk/newimages/homeicon.png")
    # photo = ImageTk.PhotoImage(home_logo)

    # home_logo_label = Label(image=photo,font=(1))
    # home_logo_label.place(x=25,y=60)
    
    mydetails_btn=Button(frame0,text='MY DETAILS',font=("Times new Roman",10),bg='#E6BBAD',bd=0,highlightbackground='BLACK',highlightthickness=1,command=lambda:admin_details())
    mydetails_btn.place(x=25,y=375)
    
    logout_btn=Button(frame0,text='LOG OUT',font=("Times new Roman",10),bg='#E6BBAD',width=11,anchor="center",bd=0,highlightbackground='BLACK',highlightthickness=1,command=lambda:logout())
    logout_btn.place(x=25,y=425)
    
    frame0.place(x=0,y=0) 
    
    
    
    #FRAME1 FUNCTIONALITIES FRAME
    frame1=Frame(window,width=850,height=500,bg="#FC9E4F")
    frame1.place(x=150,y=0) 
    
    #ADDING LOGO TO THE RIGHT SIDE CORNER OF THE FRAME
    logo = Image.open("customtk/newimages/fmslogo.png")
    photo = ImageTk.PhotoImage(logo)

    logo_label = Label(image=photo,font=(1))
    logo_label.place(x=900,y=5,width=100,height=90)


      
    img_f2=Image.open("customtk/newimages/whitebg.jpg")
    photo_f2=ImageTk.PhotoImage(img_f2)
    frame1_image_label=Label(frame1,image=photo_f2)
    frame1_image_label.place(x=0,y=0) 
    
    
    Font_tuple = ("Times new Roman", 20)
    frame1_text_Label=Label(frame1,text="ADMIN FUNCTIONS",font=(Font_tuple),bg="WHITE")   
    frame1_text_Label.place(relx=0.35,rely=0.035)
    
    #ADMIN MENU FRAME ITEMS
    
    #MYDETAILS
    #Everything required is imported from another file

    #LOGOUT
    def logout():
        ans=messagebox.askquestion('LOGOUT',"Are you sure you want to logout?")
        if ans == 'yes':
            messagebox.showinfo('',"You have successfully logged out.")
            time.sleep(1)
            window.destroy()
        else:
            pass 
    
    
    #ADDING IMAGEICONS TO ADMIN FUNCTIONALITIES 
    #ADD FLIGHTS
    img1=Image.open("customtk/Images/1.jpg")
    photo1=ImageTk.PhotoImage(img1)
    
    add_flights_button=Button(frame1,image=photo1,bg="BLACK",font=("bold",10),command=lambda:admin_add_flights())
    add_flights_button.place(relx=0.10,rely=0.20)
    
    add_flights_text_label=LabelFrame(frame1,text="ADD FLIGHTS",bg="#ADD8E6")
    add_flights_text_label.place(relx=0.250,rely=0.20)
    
    add_flights_desc=Message(add_flights_text_label,text="This allows you to update the system by adding new available flights.",font=("Helvetica",10))
    add_flights_desc.pack()


    
    #CANCEL FLIGHTS
    img2=Image.open("customtk/Images/6.jpg")
    photo2=ImageTk.PhotoImage(img2)
    
    cancel_flights_button=Button(frame1,image=photo2,bg="BLACK",font=("bold",10),command=lambda:admin_cancel_flights())
    cancel_flights_button.place(relx=0.6,rely=0.20)
    
    cancel_flights_text_label=LabelFrame(frame1,text="CANCEL FLIGHTS",bg="#ADD8E6")
    cancel_flights_text_label.place(relx=0.750,rely=0.20)
    
    cancel_flights_desc=Message(cancel_flights_text_label,text="This allows you to update the system by removing the cancelled flights.",font=("Helvetica",10))
    cancel_flights_desc.pack()
    
    
    #UPDATE FLIGHTS
    img3=Image.open("customtk/Images/7.png")
    photo3=ImageTk.PhotoImage(img3)
    
    update_flights_button=Button(frame1,image=photo3,font=("bold",10),command=lambda:admin_update_flights())
    update_flights_button.place(relx=0.10,rely=0.65)
    
    update_flights_text_label=LabelFrame(frame1,text="UPDATE FLIGHTS",bg="#ADD8E6")
    update_flights_text_label.place(relx=0.250,rely=0.65)
    
    update_flights_desc=Message(update_flights_text_label,text="This allows you to update the flights information regrading their status.",font=("Helvetica",10))
    update_flights_desc.pack()
    
    
    #PASSENGER INFO
    img4=Image.open("customtk/Images/8.jpg")
    photo4=ImageTk.PhotoImage(img4)
    
    passenger_info_button=Button(frame1,image = photo4,bg="BLACK",font=("bold",10),command=lambda:admin_passenger_info())
    passenger_info_button.place(relx=0.60,rely=0.65)
    
    passenger_info_text_label=LabelFrame(frame1,text="PASSENGER INFO",bg="#ADD8E6")
    passenger_info_text_label.place(relx=0.750,rely=0.65)
    
    passenger_info_desc=Message(passenger_info_text_label,text="This allows you to check and review details of the passengers & their information.",font=("Helvetica",10))
    passenger_info_desc.pack()
    
    window.mainloop()
    
admin_page()