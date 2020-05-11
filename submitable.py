import cv2
import os
import numpy as np
#import serial 
from datetime import datetime

data_1="hi" 
names=["Ayush","Ayush","Ayush","Ayush","Ayush","Ayush","Ayush"]
#def pin():
  #   ser=serial.Serial('COM6',9600)
   #  i=1
    # ser.write(i)
def detection(img):
    face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    checker=1
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    if(len(faces)==0):
        checker=0
        return None,None,0
    (x,y,w,h)=faces[0]
    return gray[y:y+h,x:x+h],faces[0],1

def file(name_of_person):
    fh=open("data.txt","a")
    date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    fh.write("%s %s\n"%(name_of_person,date))
    fh.close
    
    return 0
def training(task1):
    
    dirs = os.listdir(task1)
    faces=[]
    folders=[]
    for folder_name in dirs:
        label=int(folder_name)
        pics = task1+ "/" + folder_name
        all_pics = os.listdir(pics)
        for pics_name in all_pics:
                pic_path = pics + "/" + pics_name
                image = cv2.imread(pic_path)
                cv2.resize(image, (400, 500))
                cv2.waitKey(100)
                face, rect,checker = detection(image)
                if face is not None:
                   faces.append(face)
                   folders.append(label)
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    return faces, folders
print("wait")
faces, folders = training("images")
print("Total faces: ", len(faces))
print("Total folders: ", len(folders))

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(faces, np.array(folders))

def draw_rectangle(img, rect):
     (x, y, w, h) = rect
     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
def draw_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)

def recognize(test_img):
    img = test_img.copy()
    global data_1
    face, rect,checker = detection(test_img)
    if(checker==1):
        label,confidence= face_recognizer.predict(face)
        draw_rectangle(test_img, rect)
        print(confidence)
        if(confidence<60):
            name_of_person = names[label]
            draw_text(test_img, name_of_person, rect[0], rect[1]-5)
            if(name_of_person!=data_1):
                file(name_of_person)
            data_1=name_of_person
           # pin()
                
            return test_img,1
        else:
            
            return None,0
    else:
        return None,0
cap=cv2.VideoCapture(0)
k=cv2.waitKey(1)
while(1):
    ret,img=cap.read()
    recog_img1,checker = recognize(img)
    if(checker==1):
        cv2.imshow(names[0],recog_img1)
        k=cv2.waitKey(1)
        if(k==27):
            break;
    else:
        face,rect,checker=detection(img)
        cv2.imshow('unknown',img)
        k=cv2.waitKey(1)
        if(k==27):
            break;
        
print("recognition complete")
cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()


        

