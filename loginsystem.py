from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
class LoginSystem:

    def login(self):
        if self.username.get() == '' or self.password.get() == '':
            messagebox.showerror('Error', 'All Fields are required')
        elif self.username.get() == 'fazalullah' and self.password.get() == 'tkinter':
            messagebox.showinfo('Login Succesful', f'Welcome {self.username.get()}!')
        
        else:
            messagebox.showerror('Login Failed', 'Invalid Username or Password')

    def __init__(self, root):
        super().__init__()
        self.root = root
        self.root.title('Login System')
        self.root.geometry('1350x700+0+0')
        self.root.resizable(False,False)
        

        #Username and Password Variables
        self.username = StringVar()
        self.password = StringVar()

        #**** Images ****
        #Background Image
        self.bg = ImageTk.PhotoImage(file='E:/Documents/Python/LoginSystem/bg.jpg')
        self.bgImage = Label(self.root, image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #Declaring User, Pass & Logo Icons
        self.user_icon = PhotoImage(file="E:/Documents/Python/LoginSystem/user.png")
        self.pass_icon = PhotoImage(file="E:/Documents/Python/LoginSystem/pass.png")
        self.logo_icon = PhotoImage(file="E:/Documents/Python/LoginSystem/logo.png")

        #Title
        title=Label(self.root, text="Login System", font=('times new roman', 20,'bold'), bg='#22d9e6').place(x=0, y=0, relwidth=1)
        # btn_height = Button(self.root, text="50px high")
        # btn_height.place(height=50, x=200, y=200)
        # Login Frame
        loginFrame = Frame(self.root, bg='#22d9e6')
        loginFrame.place(x=500, y=250)

        loginLabel = Label(loginFrame, image=self.logo_icon).grid(row=0, column=0, columnspan=2, pady=20)
        #User, Password Label & Entry 
        labelUser = Label(loginFrame, text='User Name', image=self.user_icon, compound=LEFT, font=('times new roman', 10), bg='#22d9e6').grid(row=1,column=0, padx=20,pady=10)
        
        entryUser = Entry(loginFrame, bd=5, textvariable=self.username, relief=GROOVE, font=('times new roman', 15)).grid(row=1, column=1, padx=20)

        labelPass = Label(loginFrame, text='Password', image=self.pass_icon, compound=LEFT, font=('times new roman', 10), bg='#22d9e6').grid(row=2,column=0, padx=20,pady=10)

        entryPass = Entry(loginFrame, bd=5, textvariable=self.password, relief=GROOVE, font=('times new roman', 15)).grid(row=2, column=1, padx=20)
        
        loginButton = Button(loginFrame, text="Login", command= self.login, width=15, font=('times new roman', 15), bg='#22d9e6', fg='#02302a').grid(row=3, column=1, pady=10)
    

root = Tk()


window = LoginSystem(root)
root.mainloop()
