import cv2
import numpy as np
import cv2.aruco as aruco
import re

font = cv2.FONT_HERSHEY_SIMPLEX

dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_ARUCO_ORIGINAL)

cap = cv2.VideoCapture('tentativa1.mov')

ListaBlob = {}

try: 
    fh = open('file.txt', 'w') 
except FileNotFoundError: 
    fh= open("file.txt","w+")
    pass
    open('file.txt', 'w').close()

while True:

    ret, frame = cap.read()
    #frame = cv2.resize(img, (500,500))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.putText(frame,'Detection with ArUco Kilobots@UFSC',(50,50), font, 1,(0,0,0),1,cv2.LINE_AA)


    res = aruco.detectMarkers(gray, dictionary) #res[0] refere-se aos corners e res[1] aos IDs

    Corners = str(0 if res[0] is None else res[0])
    Corners = [int(s) for s in re.findall(r'\d+', Corners)]

    IDs = str(0 if res[1] is None else res[1])
    IDs = [int(s) for s in re.findall(r'\d+', IDs)]

    if len(res[0]) > 0:
        i = int(len(Corners)/9)

        for c in range(i):
            x1 = Corners[0+9*c] + Corners[2+9*c]
            x2 = Corners[4+9*c] + Corners[6+9*c]
            x = int(((x1 + x2)/4))

            y1 = Corners[1+9*c] + Corners[3+9*c]
            y2 = Corners[5+9*c] + Corners[7+9*c]
            y = int(((y1 + y2)/4))

            #if not IDs[c] in ListaBlob:
            ListaBlob[IDs[c]] = (x,y)

            print(ListaBlob)
            fh.write(str(IDs[c]) + ' ' + 'Coor: ' + str(x) + ',' + str (y) + '\r')
            cv2.circle(frame,(x, y), 30, (0,255,0), 1)
            cv2.putText(frame,str(IDs[c]),(x,y), font, 1,(255,255,255),2,cv2.LINE_AA)
            
            # aruco.drawDetectedMarkers(frame,res[0],res[1])


    cv2.imshow('arUco', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()