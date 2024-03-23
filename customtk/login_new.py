from PIL import Image, ImageTk
from tkinter import *
import customtkinter
from tkinter import messagebox
import mysql.connector
import mysql


def forget_pwd():
    def change_password():
        if username2.get() == '' or passwd4.get() == '' or cpasswd1.get() == '': 
            messagebox.showerror('Error', 'All Fields Are Required', parent=app)
        elif passwd4.get() != cpasswd1.get():
            messagebox.showerror('Error', 'Password and Confirm Password are not matching', parent=app)
        else:   
            con = mysql.connector.connect(host='localhost', user='root', password='@advance#1011', database="flightsys")
            mycursor = con.cursor()
            query = 'SELECT * FROM users WHERE username = %s'
            mycursor.execute(query, (username2.get(),))
            value = mycursor.fetchone()
            if value is None:
                messagebox.showerror('Error', 'Incorrect Username', parent=app)
            else:
                query = 'UPDATE users SET password = %s WHERE username = %s'
                mycursor.execute(query, (passwd4.get(), username2.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Password Changed Successfully', parent=app)
                app.destroy()

    def pwd1_enter(event):
        if passwd4.get() == 'New Password':
            passwd4.delete(0, 'end')
    
    def pwd2_enter(event):
        if cpasswd1.get() == 'Confirm New Password':
            cpasswd1.delete(0, 'end')

    app = Toplevel()
    app.title("RESET PASSWORD")
    app.geometry("500x500")
    app.resizable(0, 0)

    bgImage = ImageTk.PhotoImage(file='reset.jpg')
    bgLabel = Label(app, image=bgImage)
    bgLabel.place(x=0.4, y=0.4)

    heading = Label(app, text='(Your Username)', font=('arial', 9), bg='#AACBFF', fg='#000000')
    heading.place(x=210, y=220)

    username2 = Entry(app, width=17, font=('Microsoft PhagsPa', 11), bd=0, bg='#ffffff', fg='#080808')
    username2.place(x=214, y=195)
    username2.insert(0, "")

    passwd4 = Entry(app, width=17, font=('Microsoft PhagsPa', 11), bd=0, bg='#ffffff', fg='#080808')
    passwd4.place(x=214, y=246)
    passwd4.insert(0, "New Password")
    passwd4.bind('<FocusIn>', pwd1_enter)

    cpasswd1 = Entry(app, width=22, font=('Microsoft PhagsPa', 9), bd=0, bg='#ffffff', fg='#080808')
    cpasswd1.place(x=215, y=281)
    cpasswd1.insert(0, "Confirm New Password")
    cpasswd1.bind('<FocusIn>', pwd2_enter)

    resetButton = Button(app, width=13, text='Set Password', font=('Montesrrat', 12, 'bold'), bd=0, fg="#ffffff", bg='#007CFF', 
                         activebackground='#007CFF', activeforeground='#ffffff', cursor='hand2', command=change_password)
    resetButton.place(x=215, y=320)

    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    window_width = 500
    window_height = 500
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    app.geometry(f"{window_width}x{window_height}+{x}+{y}")
    app.mainloop()



def login_user():
    if username1.get()=='' or passwd.get()=='':
        messagebox.showerror('Error','All fields are required')
        
    else:
        try:
            con=mysql.connector.connect(host='localhost', user='root',password='@advance#1011', database="flightsys")
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error', 'Database connection failure')
        
        # query= 'use flightsys'
        # mycursor.execute(query)
        # query='select * from users where username=%s and password=%s'
        # mycursor.execute(query,(username1.get(),passwd.get()))
        # nodata=mycursor.fetchone()
        # if nodata==None:
        #     messagebox.showerror('Error', 'No Username exists or invalid login credentials')
        # else:
        #     messagebox.showinfo('Welcome aboard','Login successful')
        try:
            query = 'SELECT * FROM users WHERE username = %s AND password = %s'
            mycursor.execute(query, (username1.get(), passwd.get()))
            result = mycursor.fetchone()
            if result is None:
                messagebox.showerror('Error', 'Invalid username or password')
            else:
                messagebox.showinfo('Welcome aboard', 'Login successful')
        except mysql.connector.Error as e:
            messagebox.showerror('Error', f'Error during login: {e}')
        finally:
            if con.is_connected():
                mycursor.close()
                con.close()
            
            
def signup_page():
    app.destroy()
    import signup



def user_enter(event):
    if username1.get()=='Username :':
        username1.delete(0,END)

def pwd_enter(event):
    if passwd.get()=='Password :':
        passwd.delete(0,END)
                
show_password = False
def hide():
     global show_password
     show_password = not show_password
     if show_password:
        passwd.config(show='')
        openeye.config(file='openeye.png')
     else:
        openeye.config(file='closeye.png')
        passwd.config(show='*')
    #  passwd.config(show='*')

app=Tk()
app.title("Fly with FMS")
app.geometry("800x550")
app.resizable(0,0)

bgImage=ImageTk.PhotoImage(file='loginpage.jpg')

bgLabel=Label(app,image=bgImage)
bgLabel.place(x=0.4,y=0.4)

frame1=customtkinter.CTkFrame(app,fg_color="#b1f2ff", corner_radius=10, height=345,width=300)
frame1.place(x=500,y=90)

heading=Label(app, text='SKYWARD LOGIN', font=('Baskerville Old Face', 20,'bold') ,bg='#b1f2ff',fg='#104E8B')
heading.place(x=523,y=90)

username1=Entry(app,width=20,font=('Montserrat', 13, 'bold'), bd=0, bg='#b1f2ff' ,fg='#080808')
username1.place(x=505,y=170)
username1.insert(0,'Username :')

username1.bind('<FocusIn>', user_enter)

frame2=Frame(app,width=270,height=2.3, bg='#555555')
frame2.place(x=505,y=190)

passwd=Entry(app,width=20,font=('Montserrat', 13, 'bold'), bd=0, bg='#b1f2ff' ,fg='#080808')
passwd.place(x=505,y=240)
passwd.insert(0,'Password :')

passwd.bind('<FocusIn>', pwd_enter)

frame3=Frame(app,width=270,height=2.3, bg='#555555')
frame3.place(x=505,y=260)

#Passwordicon
openeye=PhotoImage(file='openeye.png')
eyeButton=Button(app, image=openeye, bd=0, bg='#b1f2ff', activebackground='#b1f2ff', cursor='hand2', command=hide)
eyeButton.place(x=750,y=230)

forgetButton=Button(app, text='Forget Password?', bd=0, bg='#b1f2ff', activebackground='#b1f2ff', cursor='hand2',command=forget_pwd)
forgetButton.place(x=680,y=270)

#login
loginButton=customtkinter.CTkButton(app, text='Login', corner_radius=10,font=('Montserrat',16, 'bold'),
                                    fg_color='#080808',bg_color='#b1f2ff',hover_color='#104E8B',command=login_user)
loginButton.place(x=580,y=330)

makeacc=Label(app, text="Don't have an account? ", font=('Arial', 12, 'bold'), bg='#b1f2ff',fg='#080808')
makeacc.place(x=513,y=380)

#signup_button
signupButton=Button(app, text='SIGN UP',font=('Montesrrat',12,'bold','underline'), bd=0, fg="#104E8B",bg='#b1f2ff', 
                    activebackground='#b1f2ff', activeforeground='#104E8B',cursor='hand2', command=signup_page)
signupButton.place(x=700,y=378)














# Center the window on the desktop
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
window_width = 850
window_height = 570
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
app.geometry(f"{window_width}x{window_height}+{x}+{y}")

app.mainloop()