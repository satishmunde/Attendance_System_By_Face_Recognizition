from tkinter import *
from PIL import Image,ImageTk
from datetime import datetime
import time
import pandas as pd
import seaborn as sns




class Dashboard:
    def __init__(self,window):
        self.window=window
        self.window.title('Dashboard')
        self.window.geometry('1366x768')
        self.window.state('zoomed')
        self.window.config(background='#eff5f6')

        
        self.header = Frame(self.window,bg='#009df4')
        self.header.place(x=300,y=0,width=1070,height=60)
        
        self.logout_text = Button(self.window,text='Logout',bg='#32cf8e',font=("",13,'bold'),bd=1,fg='white',cursor='hand2',activebackground='#32cf8e')
        self.logout_text.place(x=950,y=15)
        
        
        self.slide_bar=Frame(self.window,bg='white')
        self.slide_bar.place(x=325,y=70)
        
        
        self.heading = Label(self.window,text='DashBoard',font=('',13,'bold'),fg='#0064d3',bg='#eff5f6')
        self.heading.place(x=325,y=70)
    #   -------------------------------------------------------------
      
        self.bodyFrame1=Frame(self.window,bg='white')
        self.bodyFrame1.place(x=328,y=100,width=1040,height=350)
        
        self.bodyFrame2=Frame(self.window,bg='#009aa5')
        self.bodyFrame2.place(x=975,y=470,width=300,height=220)
        
        self.bodyFrame3=Frame(self.window,bg='#e21f26')
        self.bodyFrame3.place(x=650,y=470,width=300,height=220)
        
        
        self.bodyFrame4=Frame(self.window,bg='#ffcb1f')
        self.bodyFrame4.place(x=328,y=470,width=300,height=220)
        
    # -------------------------------------------------------------------
        
        


if __name__ == "__main__":
    window=Tk()
    Dashboard(window)
    window.mainloop()