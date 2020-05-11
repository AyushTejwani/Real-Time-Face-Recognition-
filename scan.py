import cv2
import os
i=1
pic_name='.jpg'
q=input('enter the no of folder') 
path="images/"+q+"/"
cap=cv2.VideoCapture(0)
s=50
while(s>0):
    j=str(i)
    ret,img=cap.read()
    cv2.imshow('video',img)
    cv2.imwrite(path+j+'.jpg',img)
    i=i+1
    s=s-1
    k=cv2.waitKey(1)
    if(k==27):
        break;
cv2.destroyAllWindows()
cap.release()
    
