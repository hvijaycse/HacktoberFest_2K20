import cv2 
import numpy as np 

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    edge = cv2.Canny(frame, 100,150)

    cv2.imshow('Original', frame)
    cv2.imshow('Edged', edge)

    if cv2.waitKey(25) == 27:   #Escape Key(esc)
        break   

cap.release()
cv2.destroyAllWindows()