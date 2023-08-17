from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
from PIL import Image
import os

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Photo Upload........")
        self.root.geometry("500x500+300+50")
        self.root.wm_iconbitmap("face.ico")
        
        root.resizable(False,False)
        
        self.bg=ImageTk.PhotoImage(file=r"bg\\face.gif")
        lbl_bg=Label(self.root,image=self.bg) 
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        
        
        
        delete_btn = Button(self.root,text="Upload File",command=self.upload_file,width=25,font=("Times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=2,column=2,padx=100,pady=50)
        
    def upload_file(self):
        copy_path="D:\\Attendance System\\images\\"
        file1=filedialog.askopenfilename()
        # print(file1)
        im = Image.open(file1)
        name = file1.split('.')
        
        file= name[0].split('/')
        file=file.pop()
            # print(str(file))
            
        
            # print(file1)
        path=str(copy_path)+str(file)+'.jpeg'
            # print(path)
        im.save(str(copy_path)+str(file)+'.jpeg')
 
if __name__ == "__main__":
    root=Tk()
    obj=Login_Window(root)
    root.mainloop()
