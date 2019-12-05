'''

#https://towardsdatascience.com/face-detection-in-2-minutes-using-opencv-python-90f89d7c0f81

import cv2
import numpy as np   #will help to represent our images (frames)

#create a classifier to help us in finding faces
classifier=cv2.CascadeClassifier(haarcascade_frontalface_default.xml)


#get camera
cam=cv2.VideoCapture(0)

retrieved ,frame=cam.read()



#if a frame has been read loop

while(retrieved):
    #find faces in grayscale frame
    #remember grayscale is a 2d that contains less computational info
    #thus finding faces makes quicker
    
    
    
    faces=classifier.detectMultiScale(cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY),1.3,5)
    #try changing value 1.3 and 5 makes finding face better
    
    #draw faces on 3d image
    
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)#(255,0,0) is for color of rectangle,2 is width of rectangle
    cv2.imshow(face detection(python+opencv),frame)
    cv2.waitKey(2)
    retrieved ,frame=cam.read()
cam.release()
    








import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Display
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
cap.release()
    
    
'''
import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Read the input image
img = cv2.imread('test.jpg')
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
# Display the output
cv2.imshow('img', img)
cv2.waitKey()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

