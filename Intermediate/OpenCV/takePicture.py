import cv2
#starting camera

cap=cv2.VideoCapture(1)
# 0 means using the first camera

#to check camera is open
if cap.isOpened():
    print("camera is working")
else:
    print("problem in opening camera")      


#now taking and reading input from camera
#print(cap.sum())  #this will take an image and gives the output in numpy 3d array

status,img=cap.read()  #it will take a picture

#now showing
cv2.imshow('liveshow',img)

#now writing ans saving the image taken
cv2.imwrite('new.jpg',img)

#wait for window to close
cv2.waitKey(0)   #mili/micro seconds   ---- if given 0 then image wait for infinite time till we stop it

#to close camera
cap.release()
