# from tkinter import customtk
import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    # import ttkthemes
    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True


class Toplevel1:
    def __init__(self):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font11 = "-family {fixed} -size 13 -weight bold"
        font9 = "-family {fixed} -size 9 -weight bold"

        self.top = tk.Tk()
        self.top.geometry("600x450+966+256")
        self.top.minsize(1, 1)
        self.top.maxsize(1905, 1050)
        self.top.resizable(1, 1)
        self.top.title("1.0")
        self.top.configure(relief="ridge")
        self.top.configure(background="#6e797f")

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.25, rely=0.156, relheight=0.722, relwidth=0.575)

        self.Frame1.configure(relief='flat')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(background="#515859")
        self.Frame1.configure(cursor="fleur")

        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.261, rely=0.4, height=27, relwidth=0.51)
        self.Entry1.configure(background="#737f93")
        self.Entry1.configure(font="TkFixedFont")

        self.Entry1_2 = tk.Entry(self.Frame1, show="*")
        self.Entry1_2.place(relx=0.261, rely=0.585, height=27, relwidth=0.51)
        self.Entry1_2.configure(background="#737f93")
        self.Entry1_2.configure(font="TkFixedFont")
        self.Entry1_2.configure(selectbackground="blue")
        self.Entry1_2.configure(selectforeground="white")

        self.Button1 = tk.Button(self.Frame1, command=self.LoginBackEnd)
        self.Button1.place(relx=0.406, rely=0.708, height=35, width=80)
        self.Button1.configure(background="#2377d8")
        self.Button1.configure(cursor="fleur")
        self.Button1.configure(font=font9)
        self.Button1.configure(relief="flat")
        self.Button1.configure(text='''Sign In''')

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.299, rely=0.034, height=37, width=143)
        self.Label1.configure(background="#515859")
        self.Label1.configure(cursor="fleur")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''Login''')

        self.Button1_3 = tk.Button(self.Frame1, command=self.register)
        self.Button1_3.place(relx=0.716, rely=0.852, height=35, width=90)
        self.Button1_3.configure(activebackground="#f9f9f9")
        self.Button1_3.configure(background="#d84b0f")
        self.Button1_3.configure(font="-family fixed -size 9 -weight bold -slant roman -underline 0 -overstrike 0")
        self.Button1_3.configure(relief="flat")
        self.Button1_3.configure(text='''Sign Up''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.261, rely=0.338, height=15, width=71)
        self.Label2.configure(background="#515859")
        self.Label2.configure(foreground="#a6abb2")
        self.Label2.configure(text='''Username''')

        self.Label2_4 = tk.Label(self.Frame1)
        self.Label2_4.place(relx=0.261, rely=0.523, height=15, width=71)
        self.Label2_4.configure(activebackground="#f9f9f9")
        self.Label2_4.configure(background="#515859")
        self.Label2_4.configure(cursor="fleur")
        self.Label2_4.configure(foreground="#a6abb2")
        self.Label2_4.configure(text='''Password''')

        self.menubar = tk.Menu(self.top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        self.top.configure(menu=self.menubar)
        self.top.mainloop()
        self.top = tk.Tk

    def register(self):
        '''This class configures the register window, like the geometry, 
        title and all the buttons and labels.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font10 = "-family {fixed} -size 10 -weight bold"

        self.root = tk.Tk()
        self.root.geometry("467x364+679+202")
        self.root.minsize(1, 1)
        self.root.maxsize(1905, 1050)
        self.root.resizable(1, 1)
        self.root.title("1.0")
        self.root.configure(background="#5f2282")

        self.menubar = tk.Menu(self.root, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        self.root.configure(menu=self.menubar)

        self.FrameRegister = tk.Frame(self.root)
        self.FrameRegister.place(relx=0.236, rely=0.192, relheight=0.626
                                 , relwidth=0.525)
        self.FrameRegister.configure(relief='flat')
        self.FrameRegister.configure(borderwidth="2")
        self.FrameRegister.configure(background="#ff8800")
        self.FrameRegister.configure(cursor="fleur")

        self.LabelRegister = tk.Label(self.FrameRegister)
        self.LabelRegister.place(relx=0.122, rely=0.088, height=15, width=187)
        self.LabelRegister.configure(background="#a82ac1")
        self.LabelRegister.configure(font=font10)
        self.LabelRegister.configure(foreground="#ffffff")
        self.LabelRegister.configure(text='''Create Your Account''')

        self.EntryRegister = tk.Entry(self.FrameRegister)
        self.EntryRegister.place(relx=0.265, rely=0.307, height=17, relwidth=0.473)
        self.EntryRegister.configure(background="#f4dbff")
        self.EntryRegister.configure(font="TkFixedFont")
        self.EntryRegister.configure(relief="flat")

        self.EntryRegister_1 = tk.Entry(self.FrameRegister)
        self.EntryRegister_1.place(relx=1.592, rely=0.772, height=17, relwidth=0.473)
        self.EntryRegister_1.configure(background="#f4dbff")
        self.EntryRegister_1.configure(font="TkFixedFont")
        self.EntryRegister_1.configure(relief="flat")
        self.EntryRegister_1.configure(selectbackground="blue")
        self.EntryRegister_1.configure(selectforeground="white")

        self.EntryRegister_2 = tk.Entry(self.FrameRegister)
        self.EntryRegister_2.place(relx=0.241, rely=1.167, height=17, relwidth=0.473)
        self.EntryRegister_2.configure(background="#f4dbff")
        self.EntryRegister_2.configure(font="TkFixedFont")
        self.EntryRegister_2.configure(relief="flat")
        self.EntryRegister_2.configure(selectbackground="blue")
        self.EntryRegister_2.configure(selectforeground="white")

        self.LabelRegister2 = tk.Label(self.FrameRegister)
        self.LabelRegister2.place(relx=0.265, rely=0.219, height=15, width=77)
        self.LabelRegister2.configure(background="#ff8800")
        self.LabelRegister2.configure(font=font10)
        self.LabelRegister2.configure(text='''Username:''')

        self.EntryRegister_3 = tk.Entry(self.FrameRegister, show="*")
        self.EntryRegister_3.place(relx=0.265, rely=0.491, height=17, relwidth=0.473)
        self.EntryRegister_3.configure(background="#f4dbff")
        self.EntryRegister_3.configure(cursor="fleur")
        self.EntryRegister_3.configure(font="TkFixedFont")
        self.EntryRegister_3.configure(relief="flat")
        self.EntryRegister_3.configure(selectbackground="blue")
        self.EntryRegister_3.configure(selectforeground="white")

        self.LabelRegister2_4 = tk.Label(self.FrameRegister)
        self.LabelRegister2_4.place(relx=0.265, rely=0.395, height=15, width=77)
        self.LabelRegister2_4.configure(activebackground="#f9f9f9")
        self.LabelRegister2_4.configure(background="#ff8800")
        self.LabelRegister2_4.configure(
            font="-family fixed -size 10 -weight bold -slant roman -underline 0 -overstrike 0")
        self.LabelRegister2_4.configure(text='''Password:''')

        self.ButtonRegister = tk.Button(self.FrameRegister, command=self.RegisterBackEnd)
        self.ButtonRegister.place(relx=0.327, rely=0.658, height=35, width=80)
        self.ButtonRegister.configure(background="#0088ff")
        self.ButtonRegister.configure(font=font10)
        self.ButtonRegister.configure(foreground="#ffffff")
        self.ButtonRegister.configure(relief="flat")
        self.ButtonRegister.configure(text='''Sign Up''')
        self.root.mainloop()

    def systempanel(self):
        panel = tk.Tk()
        panel.title("System Panel")
        panel.geometry("600x450+966+256")

    def RegisterBackEnd(self):
        try:
            with open("users.txt", "a") as archiveUser:
                archiveUser.write(self.EntryRegister.get() + '\n')

            with open("passwords.txt", "a") as archivePass:
                archivePass.write(self.EntryRegister_3.get() + '\n')
            self.root.destroy()
        except:
            pass

    def LoginBackEnd(self):
        with open("users.txt", "r") as archiveUser:
            users = archiveUser.readlines()
        with open("passwords.txt", "r") as archivePass:
            passws = archivePass.readlines()

        users = list(map(lambda x: x.replace('\n', ''), users))
        passws = list(map(lambda x: x.replace('\n', ''), passws))

        user = self.Entry1.get()
        passw = self.Entry1_2.get()

        sucesslogin = False

        for i in range(len(users)):
            if user == users[i] and passw == passws[i]:
                self.top.destroy()
                self.systempanel()
                sucesslogin = True

        if not sucesslogin:
            self.top.destroy()

Toplevel1()


