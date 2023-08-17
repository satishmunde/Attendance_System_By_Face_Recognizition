from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD
from turtle import update, width
from PIL import Image,ImageTk
from mysql.connector.locales.eng import client_error
import mysql.connector
import os
from upload_photo import Login_Window



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Details ")
        self.root.state('zoomed')
        self.root.wm_iconbitmap("face.ico")
        
        # root.resizable(False,False)
        
    # ---------------Veriable----------
        self.var_dept = StringVar()
        self.var_batch = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob= StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_listb = StringVar()
        self.var_textb = StringVar()
        self.search = StringVar()
        
    # bg image-------------------
        # img3 = Image.open(r" bg\\photo.jpg")
        # img3 = img3.resize((1530,710),Image.LANCZOS)
        # self.photoimg3 =ImageTk.PhotoImage(img3)
        
        # bg_img = Label(self.root,image=self.photoimg3)
        # bg_img.place(x=0,y=0,width=1530,height=710)
        title_lbl = Label(self.root,text ="Student Data Entry",font = ("Agency FB",30,"bold"),bg = "red",fg = "black")
        title_lbl.place(x=0,y=20,width=1300,height=45)

        
    # -------------- Left Label Frame ----------------
        Left_frame=LabelFrame(self.root,text="Students Details",fg = "red",bd=10,relief=RIDGE,bg='grey')
        Left_frame.place(x=5,y=100,width=570,height=500) 
        
        
    # Current cource------------------
        current_cource_frame=LabelFrame(self.root,text="Current Cource",bd=6,relief=RIDGE,bg='aqua')
        current_cource_frame.place(x=20,y=120,width=535,height=120) 
        
    # Department----------------------
        
        dep_label = Label(current_cource_frame,text = "Department",font=("Times new roman",12,"bold"))
        dep_label.grid(row=0,column= 0,padx=10)
        
        dep_combo = ttk.Combobox(current_cource_frame,textvariable=self.var_dept,font=("Times new roman",12,"bold"),width= 15)
        dep_combo["values"]=("Select Department","BCS","BCA","Bio Tech","Bio Info","Msc CS","Msc BT")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)
        
    # Batch ---------------------------
        
        Batch_label = Label(current_cource_frame,text = "Batch",font=("Times new roman",12,"bold"))
        Batch_label.grid(row=0,column= 2,padx=15)
        
        Batch_combo = ttk.Combobox(current_cource_frame,textvariable=self.var_batch,font=("Times new roman",12,"bold"),width= 15)
        Batch_combo["values"]=("Select Batch","Batch A","Batch B","Batch C")
        Batch_combo.current(0)
        Batch_combo.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
    # Year--------------------
        
        year_label = Label(current_cource_frame,text = "Year",font=("Times new roman",12,"bold"))
        year_label.grid(row=1,column= 0,padx=5,sticky=W)
        
        year_combo = ttk.Combobox(current_cource_frame,textvariable=self.var_year,font=("Times new roman",12,"bold"),width= 15)
        year_combo["values"]=("Select Year","First Year","Second Year","Third Year")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)
        
    # Semester ----------------
        
        Sem_label = Label(current_cource_frame,text = "Semester",font=("Times new roman",12,"bold"))
        Sem_label.grid(row=1,column= 2,padx=5)
        
        Sem_combo = ttk.Combobox(current_cource_frame,textvariable=self.var_semester,font=("Times new roman",12,"bold"),width= 15)
        Sem_combo["values"]=("Select Semester","Odd","Even")
        Sem_combo.current(0)
        Sem_combo.grid(row=1,column=3,padx=10,pady=10,sticky=W)
        
    # Student Information -----------------------------------
        
        class_student_frame=LabelFrame(self.root,text="Student Info",bd=6,relief=RIDGE,bg='aqua')
        class_student_frame.place(x=20,y=245,width=540,height=340)
        
    # StudentId --------------------------------
        
        StudentId_label = Label(class_student_frame,text = "Student ID",font=("Times new roman",10,"bold"))
        StudentId_label.grid(row=0,column= 0,padx=8,sticky=W)
        
        StudentId_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("Times new roman",10,"bold"))
        StudentId_entry.grid(row=0,column=1,padx=5,sticky=W)
        
        
    # Student Name ----------------------------
        
        StudentName_label = Label(class_student_frame,text = "Student Name",font=("Times new roman",10,"bold"))
        StudentName_label.grid(row=0,column= 2,padx=8,pady = 8,sticky=W)
        
        StudentId_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("Times new roman",10,"bold"))
        StudentId_entry.grid(row=0,column=3,padx=8,pady = 8,sticky=W)
        
    # Class Division ------------------------------------
        
        class_div_label = Label(class_student_frame,text = "Class",font=("Times new roman",10,"bold"))
        class_div_label.grid(row=1,column= 0,padx=8,pady = 8,sticky=W)
        
        class_div_entry = ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("Times new roman",10,"bold"))
        class_div_entry.grid(row=1,column=1,padx=8,pady=5,sticky=W)
        
    # Rolll No ---------------------------------
        
        roll_no_label = Label(class_student_frame,text = "Roll No",font=("Times new roman",10,"bold"))
        roll_no_label.grid(row=1,column= 2,padx=8,pady=8,sticky=W)
        
        roll_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("Times new roman",10,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=8,pady=8,sticky=W)
        
    # gender------------------------------------
        
        gender_label = Label(class_student_frame,text = "Gender",font=("Times new roman",10,"bold"))
        gender_label.grid(row=2,column=0,padx=8,pady=8,sticky=W)
        
        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("Times new roman",10,"bold"),width= 15)
        gender_combo["values"]=("Select Gender","Male","Female","Transgender")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=8,pady=8,sticky=W)
        
        
        
    # dob ---------------------------------
        
        dob_label = Label(class_student_frame,text = "D-O-B",font=("Times new roman",10,"bold"))
        dob_label.grid(row=2,column= 2,padx=8,pady=8,sticky=W)
        
        dob_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("Times new roman",10,"bold"))
        dob_entry.grid(row=2,column=3,padx=8,pady=8,sticky=W)
        
    # email------------------------------------
        
        email_label = Label(class_student_frame,text = "email",font=("Times new roman",10,"bold"))
        email_label.grid(row=3,column= 0,padx=6,pady = 6,sticky=W)
        
        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("Times new roman",10,"bold"))
        email_entry.grid(row=3,column=1,padx=6,pady=6,sticky=W)
        
    # phone No ---------------------------------
        
        phone_no_label = Label(class_student_frame,text = "Phone No",font=("Times new roman",10,"bold"))
        phone_no_label.grid(row=3,column= 2,padx=6,pady=6,sticky=W)
        
        phone_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("Times new roman",10,"bold"))
        phone_no_entry.grid(row=3,column=3,padx=6,pady=6,sticky=W)
        
        
    # Address ------------------------------------
        
        add_label = Label(class_student_frame,text = "Addreess",font=("Times new roman",10,"bold"))
        add_label.grid(row=4,column= 0,padx=8,pady = 8,sticky=W)
        
        add_entry = ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("Times new roman",10,"bold"))
        add_entry.grid(row=4,column=1,padx=8,pady=8,sticky=W)
        
    # Class teacher ---------------------------------
        
        Class_teacher_label = Label(class_student_frame,text = "Class Teacher",font=("Times new roman",10,"bold"))
        Class_teacher_label.grid(row=4,column= 2,padx=8,pady=8,sticky=W)
        
        Class_teacher_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("Times new roman",10,"bold"))
        Class_teacher_entry.grid(row=4,column=3,padx=8,pady=8,sticky=W)
        
        
    # -----------------radio Button ______
        
        std_photo_label = Label(class_student_frame,text = "Photo is Available",font=("Times new roman",10,"bold"))
        std_photo_label.grid(row=5,column= 0,padx=2,pady=2,sticky=W)
        
        self.var_radio1=StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Available",value="Yes")
        radiobtn1.grid(row=5,column=1)
        
       
        radiobtn2 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Not Available",value="No")
        radiobtn2.grid(row=5,column=2)
    
        
    # Buttons ----------------------------------------------
        
        btn_frame = Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=206,width=500,height=100)
        
        save_btn = Button(btn_frame,text="Save",command = self.add_data,width=25,font=("Times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,padx=2)
        
        
        update_btn = Button(btn_frame,text="Update",command = self.update_data,width=25,font=("Times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=1,column=0,padx=2)
        
        delete_btn = Button(btn_frame,text="Delete",command = self.delete_data,width=25,font=("Times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=1,padx=2)
        
        reset_btn = Button(btn_frame,text="Reset",command = self.reset_data,width=25,font=("Times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=1,column=1,padx=2)
        
        view_photo_btn = Button(btn_frame,text="View Photo",command = self.openimg,width=25,font=("Times new roman",13,"bold"),bg="green",fg="white")
        view_photo_btn.grid(row=2,column=0,padx=2)
        
        upload_photo_btn = Button(btn_frame,text="Upload Photo",command=self.upload,width=25,font=("Times new roman",13,"bold"),bg="green",fg="white")
        upload_photo_btn.grid(row=2,column = 1,padx=2)

        
        
        # -------------- Right Label Frame ----------------
        
        Right_frame=LabelFrame(self.root,text="Students Details",bd=10,relief=RIDGE,bg='grey',fg="red")
        Right_frame.place(x=600,y=100,width=650,height=500) 
        
    # # Search  System----------------------------------
        
        search_frame = LabelFrame(Right_frame,bd=2,text="Search System",relief=RIDGE,bg="aqua")
        search_frame.place(x=2,y=0,width=615,height=80)
        
        search_label = Label(search_frame,text="Search By :",font=("Times new roman",13,"bold"),width=10,bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        
        search_combo = ttk.Combobox(search_frame,textvariable=self.var_listb,font=("Times new roman",12,"bold"),width= 10)
        search_combo["values"]=("Roll No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        
        global info_entry
        
        info_entry = ttk.Entry(search_frame,textvariable=self.search,width=20,font=("Times new roman",10,"bold"))
        info_entry.grid(row=0,column=2,padx=10,pady=1,sticky=W)
        
        
        search_btn = Button(search_frame,command= self.search_data,text="Search",width=10,font=("Times new roman",8,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=10)
        
        showAll_btn = Button(search_frame,text="Show All",command=self.fetch_data,width=10,font=("Times new roman",8,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=10)
        
        
    # table Frame---------------------------------
        
        table_frame = LabelFrame(Right_frame,bd=4,relief=RIDGE,bg="yellow")
        table_frame.place(x=2,y=70,width=620,height=400)
        
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("Dept","Batch","Year","Sem","Id","Name","Class","Roll","Gender","DOB","Email","Phone","Address","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand = scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_y.config(command=self.student_table.xview)
        scroll_x.config(command=self.student_table.yview)
        
        self.student_table.heading("Dept",text="Department")
        self.student_table.heading("Batch",text="Batch")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semster")
        self.student_table.heading("Id",text="StudentId")
        self.student_table.heading("Name",text="Name")
       
        self.student_table.heading("Class",text="Class")
        self.student_table.heading("Roll",text="Roll")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="D-O-B")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone",text="Phone No")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photo",text="Photo")
        self.student_table["show"]="headings"
        
       
        
        self.student_table.column("Dept",width=100)
        self.student_table.column("Batch",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("Id",width=100)
        self.student_table.column("Name",width=100)
        
        self.student_table.column("Class",width=100)
        self.student_table.column("Roll",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Phone",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("Photo",width=100)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
      
    def upload(self):
        self.new_window=Toplevel(self.root)
        self.app = Login_Window(self.new_window)  
    # -----------------------------Function Declaratio ---------
    def add_data(self):
        if self.var_dept.get() == "Select Department" or self.var_batch.get() == "Select Batch" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_std_id.get() == "" or self.var_std_name.get() == ""or self.var_div.get() == "" or self.var_roll.get() == "" or self.var_gender.get() == ""or self.var_dob.get() == "" or self.var_email.get() == "" or self.var_phone.get() == "" or self.var_address.get() == "" or self.var_teacher.get() == "":
            messagebox.showerror("Error","All Fields are Required",parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password = "Pass@1234",database = 'face_recognizer',auth_plugin = 'mysql_native_password')
                my_cursor = conn.cursor()
                my_cursor.execute('''INSERT INTO student(Dept,Batch,Year,Semester,Student_Id,Name,Class,Roll,Gender,DOB,Email,Phone,Address,Teacher,Photo)
                                  VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(self.var_dept.get(),
                                                                                                                
                                                                                                                self.var_batch.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                               
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()
                                                                                                            ));                                                                                                             
                                                                                                                    
                                                                                                                    
                                                            
                conn.commit()
                self.fetch_data()
                
                conn.close()
                messagebox.showinfo("Sucess","Student Details had  Been Added Successfully",parent = self.root)
                self.var_std_id.set("")
                self.var_div.set("")
                self.var_std_name.set("")
                self.var_roll.set("")
                self.var_gender.set("")
                self.var_dob.set("")
                self.var_email.set("")
                self.var_phone.set("")
                self.var_address.set("")
                self.var_teacher.set("")
                self.var_radio1.set("")
            except Exception as ex:
                messagebox.showerror("Error",f"Due to :{str(ex)}",parent = self.root)

#  =--------------------------------------Fetch data----------
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password = "Pass@1234",database = 'face_recognizer',auth_plugin = 'mysql_native_password')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
            
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()       
        
    # -----------------Get Cursor----------------
    def get_cursor(self,event=""):
            cursor_focus=self.student_table.focus()
            content = self.student_table.item(cursor_focus)
            data= content["values"]
            self.var_dept.set(data[0]),
            self.var_batch.set(data[1]),
            self.var_year.set(data[2]),
            self.var_semester.set(data[3]),
            self.var_std_id.set(data[4]),
            self.var_std_name.set(data[5]),
            self.var_div.set(data[6]),
            self.var_roll.set(data[7]),
            self.var_gender.set(data[8]),
            self.var_dob.set(data[9]),
            self.var_email.set(data[10]),
            self.var_phone.set(data[11]),
            self.var_address.set(data[12]),
            self.var_teacher.set(data[13]),
            self.var_radio1.set(data[14])
        
    # -----------Update button----
    def update_data(self):
        if self.var_dept.get() == "Select Department" or self.var_batch.get() == "Select Batch" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_std_id.get() == "" or self.var_std_name.get() == ""or self.var_div.get() == "" or self.var_roll.get() == "" or self.var_gender.get() == ""or self.var_dob.get() == "" or self.var_email.get() == "" or self.var_phone.get() == "" or self.var_address.get() == "" or self.var_teacher.get() == "":
                messagebox.showerror("Error","All Fields are Required",parent = self.root)
        else:                                                                                                                               
            try:
                Update = messagebox.askyesno( "Update","Do you want to update Student Details",parent=self.root)
                if Update>0:
                    
                    conn = mysql.connector.connect(host="localhost",username="root",password = "Pass@1234",database = 'face_recognizer',auth_plugin = 'mysql_native_password')
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dept = %s,Batch=%s,Year= %s,Semester= %s,Name= %s,Class= %s,Roll= %s,Gender= %s,DOB= %s,Email= %s,Phone= %s,Address= %s,Teacher= %s, Photo=%s where student_id=%s",(
                            
                                        self.var_dept.get(),
                                        self.var_batch.get(),
                                        self.var_year.get(),
                                        self.var_semester.get(),
                                        self.var_std_name.get(),
                                        self.var_div.get(),
                                        self.var_roll.get(),
                                        self.var_gender.get(),
                                        self.var_dob.get(),
                                        self.var_email.get(),
                                        self.var_phone.get(),
                                        self.var_address.get(),
                                        self.var_teacher.get(),
                                        self.var_radio1.get(),
                                        self.var_std_id.get()
                                    ))
                    if not Update:
                        return
                messagebox.showinfo("Success","Studet Details updated successfully",parent=self.root)
                conn.commit()  
                self.fetch_data()
                conn.close()
            except Exception as ex:
                messagebox.showerror("Error",f"Due To : {str(ex)}",parent=self.root)
        
    # ------------------delete function-----------------
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student delete page","Do you want to delete this Student",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password = "Pass@1234",database = 'face_recognizer',auth_plugin = 'mysql_native_password')
                    my_cursor = conn.cursor()
                    sql="delete from student where Student_Id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
            
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted the Student Details",parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error",f"Due to : {str(ex)}",parent=self.root)
                
    # ----------reset function --------------
    def reset_data(self):
        self.var_dept.set("Select Department")
        self.var_batch.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_div.set("")
        self.var_std_name.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")                                      

    def openimg(self):
        os.startfile("images")  
     
    def open_img(self):
        conn = mysql.connector.connect(host="localhost",username="root",password = "Pass@1234",database = 'face_recognizer',auth_plugin = 'mysql_native_password')
        my_cursor = conn.cursor()
        if (self.var_listb == 0):
            # my_cursor.execute("select * from students where Roll = self.var_textb.get())
            my_cursor.execute("select * from attendanceses")
            result = my_cursor.fetchone()
            # print(result)
            for x in result:
                print(x)
                                                                                                                                        
    def search_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password = "Pass@1234",database = 'face_recognizer',auth_plugin = 'mysql_native_password')
        id = self.search.get()
        
        my_cursor = conn.cursor()    
        my_cursor.execute("select * from student where roll = %s",[(id)])
        rows = my_cursor.fetchall()
        
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values= row)    
                
            conn.commit()
        conn.close()
     
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()