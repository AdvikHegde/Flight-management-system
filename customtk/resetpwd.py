from PIL import Image, ImageTk
from tkinter import *
import customtkinter
from tkinter import messagebox
import mysql.connector
import mysql


def pwd1_enter(event):
    if passwd.get()=='New Password':
        passwd.delete(0,END)
        
def pwd2_enter(event):
    if cpasswd.get()=='Confirm New Password':
        cpasswd.delete(0,END)
        
def login_pg():
    app.destroy()
    import login_new


app=Tk()
app.title("RESET PASSWORD")
app.geometry("500x500")
app.resizable(0,0)


bgImage=ImageTk.PhotoImage(file='reset.jpg')

bgLabel=Label(app,image=bgImage)
bgLabel.place(x=0.4,y=0.4)

heading=Label(app, text='*your username*', font=('arial', 9),bg='#AACBFF',fg='#000000')
heading.place(x=210,y=220)

username1=Entry(app,width=17,font=('Microsoft PhagsPa', 11), bd=0, bg='#ffffff' ,fg='#080808')
username1.place(x=214,y=195)
username1.insert(0, "")

passwd=Entry(app,width=17,font=('Microsoft PhagsPa', 11), bd=0, bg='#ffffff' ,fg='#080808')
passwd.place(x=214,y=246)
passwd.insert(0, "New Password")
passwd.bind('<FocusIn>', pwd1_enter)

cpasswd=Entry(app,width=22,font=('Microsoft PhagsPa', 9), bd=0, bg='#ffffff' ,fg='#080808')
cpasswd.place(x=215,y=281)
cpasswd.insert(0, "Confirm New Password")
cpasswd.bind('<FocusIn>', pwd2_enter)



resetButton=Button(app, width=13,text='Set Password',font=('Montesrrat',12,'bold'), bd=0, fg="#ffffff",bg='#007CFF', 
                    activebackground='#007CFF', activeforeground='#ffffff',cursor='hand2', command=login_pg)
resetButton.place(x=215,y=320)



#setting the window in center
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
window_width = 500
window_height = 500
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
app.geometry(f"{window_width}x{window_height}+{x}+{y}")

app.mainloop()