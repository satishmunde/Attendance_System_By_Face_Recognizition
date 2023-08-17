import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import voice


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
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
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
    faces = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
    faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

    facesCurrentFrame = face_recognition.face_locations(faces)
    encodesCurrentsFrame = face_recognition.face_encodings(
        faces, facesCurrentFrame)

    for encodeFace, faceloc in zip(encodesCurrentsFrame, facesCurrentFrame):
        matches = face_recognition.compare_faces(
            encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(
            encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        eyes_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")

        first_read = True

        # Video Capturing by opening web-cam
        cap = cv2.VideoCapture(0)
        # to check for first instance of capturing it will return True and image
        ret, image = cap.read()

        while ret:
            # this will keep the web-cam running and capturing the image for every loop
            ret, image = cap.read()
            # Convert the recorded image to grayscale
            gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # Applying filters to remove impurities
            gray_scale = cv2.bilateralFilter(gray_scale, 5, 1, 1)
            # to detect face and eye
            faces = face_cascade.detectMultiScale(gray_scale, 1.3, 5, minSize=(200, 200))
            if len(faces) > 0:
                for (x, y, w, h) in faces:
                    image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    # eye_face var will be i/p to eye classifier
                    eye_face = gray_scale[y:y + h, x:x + w]
                    # image
                    eye_face_clr = image[y:y + h, x:x + w]
                    # get the eyes
                    eyes = eyes_cascade.detectMultiScale(eye_face, 1.3, 5, minSize=(50, 50))
                    if len(eyes) >= 2:
                        if first_read:
                            cv2.putText(image, "Eye's detected, press s to check blink", (70, 70), cv2.FONT_HERSHEY_SIMPLEX,
                                        1, (0, 255, 0), 2)
                        else:
                            cv2.putText(image, "Eye's Open", (70, 70), cv2.FONT_HERSHEY_SIMPLEX,
                                        1, (255, 255, 255), 2)
            
            else:
                cv2.putText(image, "No Face Detected.", (70, 70), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 255, 0), 2)

        
    
        if matches[matchIndex] and eyes == True:
            id = personName[matchIndex].upper()
            print(id)
            y1, x2, y2, x1 = faceloc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0),2)
            cv2.rectangle(frame, (x1, y2-35), (x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(frame, id, (x1 + 6, y2 - 6),cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255),2)
            MarkAttendance(id)

    cv2.imshow("Camera", frame)
    if cv2.waitKey(10) == 13:
        break
cap.release()
cv2.destroyAllWindows()

