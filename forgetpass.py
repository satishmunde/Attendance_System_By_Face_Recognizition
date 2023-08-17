from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
from turtle import update, width
import os
import register
from main import Face_Recognition_System
from mysql.connector.locales.eng import client_error
import mysql.connector



class Forget:
    def __init__(self,root):
        self.root=root
        self.root.title("Forget Password System")
        self.root.geometry('500x500+400+50')
        self.root.wm_iconbitmap("face.ico")
        
        root.resizable(False,False)
        self.var_id = StringVar()
        self.var_pass = StringVar()
        frame = Frame(root,width=500,height=660,bg="#cb6d51")
        frame.place(x=00,y=0)

        heading = Label(frame,text='Forget Password ',fg='black',bg='#cb6d51',font=('Arial',18,'bold'))
        heading.place(x=150,y=80)

        # user Name ----------------------------------------------

        def on_enter(e):
            user.delete(0,'end')
            
        def on_leave(e):
            name=user.get()
            if name=='':
                user.insert(0,'Enter Your Username')

        user = Entry(frame,width= 35,textvariable=self.var_id,fg='black',border=0,bg='#cb6d51',font=('Microsoft YaHei UI Light',13))
        user.place(x=80,y=150)
        user.insert(0,'Enter Your Username')
        user.bind('<FocusIn>',on_enter)
        user.bind('<FocusOut>',on_leave)

        Frame(frame,width=315,height=2,bg='black').place(x=80,y=175)
        
        def on_enter1(e):
            passc.delete(0,'end')
            
        def on_leave1(e):
            name=passc.get()
            if name=='':
                passc.insert(0,'Enter Your Password')
        
        passc = Entry(frame,width= 35,textvariable=self.var_pass,fg='black',border=0,bg='#cb6d51',font=('Microsoft YaHei UI Light',13))
        passc.place(x=80,y=225)
        passc.insert(0,'Enter Your Password')
        passc.bind('<FocusIn>',on_enter1)
        passc.bind('<FocusOut>',on_leave1)

        Frame(frame,width=315,height=2,bg='black').place(x=80,y=250)
        # Button-------------------------------------------------
        
        Button(frame,width=30,pady=7,text='Get Password',command=self.forgetp,bg="black",fg='#cb6d51',border=0).place(x=125,y=300)
        
        Button(frame,width=30,pady=7,text='Reset Password',command=self.resetp,bg="black",fg='#cb6d51',border=0).place(x=125,y=350)
        
    def forgetp(self):
        conn = mysql.connector.connect(host="localhost",username="root",password = "Pass@1234",database = 'face_recognizer',auth_plugin = 'mysql_native_password')
        pwd0 = self.var_id.get()
        my_cursor = conn.cursor()
        
            
        my_cursor.execute("select Password from login where User_Name = %s",[(pwd0)])
        result = my_cursor.fetchall()
        
        messagebox.showinfo("Sucess",f"Your Password is {result}")
        conn.commit()
        conn.close()

    def resetp(self):
        
        conn = mysql.connector.connect(host="localhost",username="root",password = "Pass@1234",database = 'face_recognizer',auth_plugin = 'mysql_native_password')
        id = self.var_id.get()
        pwd = self.var_pass.get()
        my_cursor = conn.cursor()
        
            
        my_cursor.execute("update login set Password = %s where User_Name=%s",[(pwd),(id)])
        
        messagebox.showinfo("Sucess",f"Your Password is Changed Sucessfully")
        conn.commit()
        conn.close()
        root.destroy()
        
if __name__ == "__main__":
    root=Tk()
    boj=Forget(root)
    root.mainloop()
