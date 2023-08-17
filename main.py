from tkinter import*
from tkinter import ttk
import tkinter
from tkinter import messagebox
from PIL import Image,ImageTk
from StudentInfo import Student
from tkinter import Frame
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import voice
from attendance1 import Attendance1

class Face_Recognition_System:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0") 
        self.root.title("face Recogniton System")
        self.root.state('zoomed')
        self.root.wm_iconbitmap("face.ico")
    # Main Page
        # img=Image.open(r"bg\\college.jfif.jpg")
        # img=img.resize((433,100),Image.LANCZOS)
        # self.photoimg=ImageTk.PhotoImage(img)
        # f_lbl=Label(self.root,image=self.photoimg)
        # f_lbl.place(x=0,y=0,width=433,height=100)
        
        # img1=Image.open(r"bg\\face.png.jpg")
        # img1=img1.resize((440,100),Image.LANCZOS)
        # self.photoimg1=ImageTk.PhotoImage(img1)
        # f_lbl=Label(self.root,image=self.photoimg1)
        # f_lbl.place(x=440,y=0,width=440,height=100)

        
        # img2=Image.open(r"bg\\mgm.jpg")
        # img2=img2.resize((435,100),Image.LANCZOS)
        # self.photoimg2=ImageTk.PhotoImage(img2)
        # f_lbl=Label(self.root,image=self.photoimg2)
        # f_lbl.place(x=860,y=0,width=435,height=100)
        
        img3=Image.open(r"bg\\face.gif")
        img3=img3.resize((1530,790),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1300,height=750)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("Times New Roman",35),bg="white",fg="Black")
        title_lbl.place(x=0,y=70,width=1300,height=45)

    # #student button
        img4=Image.open(r"bg\\std.jpg")
        img4=img4.resize((220,180),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,command=self.student_details,image=self.photoimg4,cursor="hand2") 
        b1.place(x=200,y=160,width=220,height=180)

        b1_1=Button(bg_img,text="Student Database",command=self.student_details,cursor="hand2",font=("Times New Roman",13,"bold"),bg="white",fg="Black") 
        b1_1.place(x=200,y=335,width=220,height=20)

    #Detect face button
        img5=Image.open(r"bg\\detector.jpg.jpg")
        img5=img5.resize((220,180),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.face_recog,cursor="hand2") 
        b1.place(x=535,y=160,width=220,height=180)

        b1_1=Button(bg_img,text="Face Detector",command=self.face_recog,cursor="hand2",font=("Times New Roman",13,"bold"),bg="white",fg="Black") 
        b1_1.place(x=535,y=335,width=220,height=20)

    # Attendance face button
        img6=Image.open(r"bg\\Attendance.jpg.jpg")
        img6=img6.resize((220,180),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,command=self.attendance_data,cursor="hand2") 
        b1.place(x=870,y=160,width=220,height=180)

        b1_1=Button(bg_img,text="Attendance",command=self.attendance_data,cursor="hand2",font=("Times New Roman",13,"bold"),bg="white",fg="Black") 
        b1_1.place(x=870,y=335,width=220,height=20)

    
    #Photos
        img9=Image.open(r"bg\\Photo.jpg")
        img9=img9.resize((220,180),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,command=self.open_img,cursor="hand2") 
        b1.place(x=320,y=450,width=220,height=180)

        b1_1=Button(bg_img,text="Photos",command=self.open_img,cursor="hand2",font=("Times New Roman",13,"bold"),bg="white",fg="Black") 
        b1_1.place(x=320,y=625,width=220,height=20)

        
    #Exit
        img11=Image.open(r"bg\\exit.jfif.jpg")
        img11=img11.resize((220,180),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,command=self.Exit,cursor="hand2") 
        b1.place(x=780,y=450,width=220,height=180)

        b1_1=Button(bg_img,text="Exit",command=self.Exit,cursor="hand2",font=("Times New Roman",13,"bold"),bg="white",fg="Black") 
        b1_1.place(x=780,y=625,width=220,height=20)
        
        
    # ---------------------Function buttons--------------------------
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app = Student(self.new_window)  
        
    def face_recog(self):
        path = 'images'
        images = []
        personName = []
        myList = os.listdir(path)
        for cu_img in myList:
            current_Img = cv2.imread(f'{path}/{cu_img}')
            images.append(current_Img)
            personName.append(os.path.splitext(cu_img)[0])
        # print(personName)

        def faceEncodings(images):
            encodeList = []
            for img in images:
                img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                encode = face_recognition.face_encodings(img)[0]
                encodeList.append(encode)
            return encodeList
        encodeListKnown = faceEncodings(images)
        # print(faceEncodings(images))
        # print("All Encodings Complated")

        def MarkAttendance(id):
            already_in_file = set()
            with open('Attendance Report\\Attendance.csv', "r") as g:      
                for line in g:
                    already_in_file.add(line.split(",")[0])

        # process your current entry:
            if id not in already_in_file:
                with open('Attendance Report\\Attendance.csv', "a") as g:   
                    now = datetime.now()
                    tString = now.strftime('%H:%M:%S')
                    dString = now.strftime('%d:%m:%y')
                    g.writelines(f'\n{id},{tString},{dString} ,Present')
                    voice.Speak(f"Roll Number {id} Your Attendance is Marked")
                
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            faces = cv2.resize(frame, (0,0), None, 0.25, 0.25)
            faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)
            
            facesCurrentFrame = face_recognition.face_locations(faces)
            encodesCurrentsFrame = face_recognition.face_encodings(faces,facesCurrentFrame)
            
            for encodeFace, faceloc in zip(encodesCurrentsFrame,facesCurrentFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                matchIndex = np.argmin(faceDis)
                
                if matches[matchIndex]:
                    id= personName[matchIndex].upper()
                    # print(id)
                    y1,x2,y2,x1 = faceloc
                    y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                    cv2.rectangle(frame, (x1,y1),(x2,y2), (0,255,0),2)
                    cv2.rectangle(frame,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                    cv2.putText(frame,id,(x1 + 6,y2 - 6),cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255),2)
                    MarkAttendance(id)
                    
            cv2.imshow("Camera",frame)
            if cv2.waitKey(10) == 13:
                break
        cap.release()
        cv2.destroyAllWindows()
        self.new_frame = Toplevel(self.root)
    
    def open_img(self):
        os.startfile("images")   
           
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance1(self.new_window)
     
    def Exit(self):
        iExit=messagebox.askyesno("Face Recognization","Are You want to Exit this Project",parent=self.root) 
        if iExit >0:
            self.root.destroy()
        else:
            return
        

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()