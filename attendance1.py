from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD
from turtle import update, width
from PIL import Image,ImageTk
from mysql.connector.locales.eng import client_error
import mysql.connector
import csv
import os
from tkinter import filedialog
import pymysql



mydata=[]
class Attendance1:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Manage Attendance")
        self.root.wm_iconbitmap("face.ico")
        self.root.state('zoomed')
        # root.resizable(False,False)
    # ------------------Variable---------------------
        
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dept=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        # self.var_atten_id=StringVar()

    # home page
       
        
        title_lbl=Label(self.root,text="ATTENDANCE MANAGEMENT SYSTEM",font=("Times New Roman",35),bg="grey",fg="skyblue")
        title_lbl.place(x=0,y=20,width=1330,height=45)

        main_frame=Frame(self.root,bd=2,bg="steelblue")
        main_frame.place(x=0,y=90,width=1480,height=600)
    
            #buttons frame 
        btn_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white") 
        btn_frame.place(x=1050,y=150,width=175,height=35) 

        imp_btn=Button(btn_frame,text = " Import csv " ,command=self.importcsv, width = 16 , font = ( "times new roman " , 13 , " bold " ) , bg = "orange", fg ="white")
        imp_btn.grid(row=0,column=0)
        
        btn2_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white") 
        btn2_frame.place(x=1050,y=250,width=175,height=35) 
        
        save_btn=Button(btn2_frame,text = " Close " ,command=self.clear, width = 16 , font = ( "times new roman " , 13 , " bold " ) , bg = "orange", fg ="white")
        save_btn.grid(row=0,column=1)


      
    #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="lavender",relief=RIDGE,text="Attendance Details")
        Right_frame.place(x=10,y=10,width=1000,height=580)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white") 
        table_frame.place(x=5,y=5,width=990,height=555)
        
        # -----------scroll 
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("roll","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("roll",text="Roll")    
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="attendance")


        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("roll",width=50)
       
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
       
    def fetchdata(self,rows):
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for i in rows:
                self.AttendanceReportTable.insert("",END,values=i)

    def importcsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir= os.getcwd(),title="Open CSV",filetypes=(("CSV file","*csv"),("ALL Files","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)
            
    def savetodb(self):
        csv_data= csv.reader(file('Attendance Report \\ Attendance.csv'))

        conn = mysql.connector.connect(host="localhost",username="root",password = "Pass@1234",database = 'face_recognizer',auth_plugin = 'mysql_native_password')
        my_cursor = conn.cursor()
        sql=f"INSERT INTO  attandance  VALUES({csvfile})"
        cursor.execute(sql)
        conn.commit()

       
        # for row in csv_data:
        #     sql="INSERT INTO  daily_n (Roll,Time,Date,Attendance) VALUES()"
        #     cursor.execute(sql)
        #     conn.commit()

        cursor.close()
        
        
    
    def clear(self):
        
        f = open("Attendance Report\\Attendance.csv", "w")
        f.truncate()
        f.close()
        
        messagebox.showinfo("Face Recognization","Attendance View Page will be close",parent=self.root) 
    

        
   
if __name__ == "__main__":
    root=Tk()
    obj=Attendance1(root)
    root.mainloop()