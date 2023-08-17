import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\\Users\\munde\\AppData\\Local\\Programs\\Python\\Python310\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\\Users\\munde\\AppData\\Local\\Programs\\Python\\Python310\\tcl\\tk8.6"
# os.environ['SQL_LIBRARY'] = r"C:\\Users\\munde\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\sqlite3"

executables = [cx_Freeze.Executable("home12.py", base=base, icon="face.ico")]


cx_Freeze.setup(
    name = "Attendance System",
    options = {"build_exe": {"packages":["tkinter","os","turtle","PIL","mysql","mysql.connector","csv","cv2","numpy","face_recognition","datetime","playsound","pyttsx3","voice"], "include_files":["face.ico",'tcl86t.dll','tk86t.dll', 'images','Attendance Report','bg','database']}},
    version = "1.0",
    description = "Attendance System | Developed By Satish Munde And Team",
    executables = executables
    )
