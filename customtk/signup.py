from tkinter import *
import customtkinter
import pymysql
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import mysql


def clear():

    email1.delete(0,END)
    username1.delete(0, END)
    passwd.delete(0, END)
    cpasswd.delete(0, END)
    check.set(0)

def con_database():
    if email1.get()=='' or username1.get()=='' or passwd.get()=='' or cpasswd.get()=='':
        messagebox.showerror('Error', 'All fields are mandatory')
    elif passwd.get() != cpasswd.get():
        messagebox.showerror('Error',"Check your password")
    elif check.get()==0:
        messagebox.showerror('Error',"Please accept terms and conditions")
    else:
       
        try:
            conn = mysql.connector.connect(host='localhost', user='root', password='@advance#1011', database="flightsys")
            mycursor = conn.cursor()

            # Ensure table exists or create it if not
            mycursor.execute('CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, email VARCHAR(50), username VARCHAR(50), password VARCHAR(20))')
            
               # Check if username already exists
            query = 'SELECT * FROM users WHERE username = %s'
            mycursor.execute(query, (username1.get(),))
            existing_user = mycursor.fetchone()
            if existing_user:
                messagebox.showerror('Error', 'Username already exists')
                conn.close()
                return
            
            # Insert data into the table
            query = 'INSERT INTO users (email, username, password) VALUES (%s, %s, %s)'
            data = (email1.get(), username1.get(), passwd.get())
            print("Data to be inserted:", data)  # Print data to be inserted for debugging
            mycursor.execute(query, data)
            conn.commit()

            print("Data insertion successful")  # Print success message for debugging

            conn.close()
            messagebox.showinfo('Success', 'Registration successful')
            clear()
            app.destroy()
            import login_new
        except Exception as e:
            messagebox.showerror('Error', f'Data insertion error: {e}')
    
    
    
    
def login_page():
    app.destroy()    
    import login_new
      

app=Tk()
app.title("Fly with FMS")
app.geometry("800x550")
app.resizable(0,0)

bgImage=ImageTk.PhotoImage(file='images/backgd.png')

bgLabel=Label(app,image=bgImage)
bgLabel.place(x=0.4,y=0.4)

frame1=customtkinter.CTkFrame(app,fg_color="#C3F4FE", corner_radius=10, height=360,width=300)
frame1.place(x=470,y=130)

heading=Label(app, text='CREATE YOUR ACCOUNT', font=('Baskerville Old Face', 16,'bold'),bg='#ffffff',fg='#104E8B')
heading.place(x=480,y=100)

email1=Label(app,text='Email :', font=('Montserrat',14,'bold'), bd=0, bg='#C3F4FE' ,fg='#080808' )
email1.place(x=480,y=140)
email1=Entry(app,width=31,font=('Microsoft PhagsPa', 13), bd=0, bg='#104E8B' ,fg='#ffffff')
email1.place(x=480,y=166)

username1=Label(app,text='Username :', font=('Montserrat',14,'bold'), bd=0, bg='#C3F4FE' ,fg='#080808' )
username1.place(x=480,y=200)
username1=Entry(app,width=31,font=('Microsoft PhagsPa', 13), bd=0, bg='#104E8B' ,fg='#ffffff')
username1.place(x=480,y=225)

passwd=Label(app,text='Password :', font=('Montserrat',14,'bold'), bd=0, bg='#C3F4FE' ,fg='#080808' )
passwd.place(x=480,y=260)
passwd=Entry(app,width=31,font=('Microsoft PhagsPa', 13), bd=0, bg='#104E8B' ,fg='#ffffff')
passwd.place(x=480,y=285)

cpasswd=Label(app,text='Confirm Password :', font=('Montserrat',14,'bold'), bd=0, bg='#C3F4FE' ,fg='#080808' )
cpasswd.place(x=480,y=320)
cpasswd=Entry(app,width=31,font=('Microsoft PhagsPa', 13), bd=0, bg='#104E8B' ,fg='#ffffff')
cpasswd.place(x=480,y=345)


check=IntVar()
termsandconditions=Checkbutton(app, text='I agree to the Terms & Conditions', font=('Eras Bold ITC',11),
                    fg='#104E8B', bg='#C3F4FE', activebackground='#C3F4FE', activeforeground='#104E8B' ,cursor='hand2', variable=check)
termsandconditions.place(x=480,y=380)

signupButton=customtkinter.CTkButton(app, text='SignUp', corner_radius=10,font=('Montserrat',16, 'bold'),
                                    fg_color='#002244',bg_color='#b1f2ff', command=con_database)
signupButton.place(x=550,y=420)

#get back to login
makeacc=Label(app, text="Already have an account? ", font=('Arial', 12, 'bold'), bg='#C3F4FE',fg='#080808')
makeacc.place(x=495,y=460)

#signup_button
signupButton=Button(app, text='Login',font=('Montesrrat',12,'bold','underline'), bd=0, fg="#104E8B",bg='#C3F4FE', 
                    activebackground='#C3F4FE', activeforeground='#104E8B',cursor='hand2',command=login_page)
signupButton.place(x=695,y=455)








screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
window_width = 800
window_height = 550
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
app.geometry(f"{window_width}x{window_height}+{x}+{y}")

app.mainloop()
