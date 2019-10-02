import cv2

#calling classifier
faceClasifier=cv2.CascadeClassifier('face.xml')
#loading video VideoCapture
cam=cv2.VideoCapture(0)

while cam.isOpened():
    frame=cam.read()[1]

    #now applying classifier
    face=faceClasifier.detectMultiScale(frame,1.13,5)  # classifer tuneing parameter
    #face is in format x,y(intital) and height and width
    for x,y,h,w in face:
        cv2.rectangle(frame,(x,y),(x+h,y+w),(0,0,255),3)
    cv2.imshow('face',frame)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()
cam.release()
