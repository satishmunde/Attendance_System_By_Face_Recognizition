from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
from turtle import update, width
import os
from login1 import Login
from register import Register 





class Home:
    def __init__(self,root):
        self.root=root
        self.root.title("Home Page")
        self.root.geometry('1530x790')
        self.root.state('zoomed')
        self.root.wm_iconbitmap("face.ico")
        
        # root.resizable(False,False)
        img3=Image.open(r"bg\\homebg.jpg")
        img3=img3.resize((1530,810),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1300,height=750)
        
        title_lbl1=Label(self.root,text="MGM's College of CS & IT Nanded",font=("Times New Roman",28),fg="#728fce")
        title_lbl1.place(x=0,y=50,width=1300,height=45)
        
        home = Menu(root)
        Attendance = Menu(home,tearoff=5)
        home.add_cascade(label="Student Attendance",menu=Attendance)
        Attendance.add_command(label="Register",command=self.register1,font=("Times New Roman",20))
        Attendance.add_command(label="Login",command=self.login,font=("Times New Roman",20))
        
        root.config(menu = home)
      
    def login(self):
        self.new_window=Toplevel(self.root)
        self.app = Login(self.new_window)  
    
    def register1(self):
        self.new_window=Toplevel(self.root)
        self.app = Register(self.new_window)  

if __name__ == "__main__":
    root=Tk()
    obj=Home(root)
    root.mainloop()
