import cv2

######################################
frameWidth = 640
frameHeight = 480
nPlateCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')
minArea = 500
color = (255, 0, 255)
######################################
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 100)
count=0
while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in numberPlates:
        area = w*h
        if area>minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv2.putText(img,'Number Plates',(x,y-5),cv2.FONT_HERSHEY_PLAIN,1,color,2)

            imgRoi = img[y:y+h, x:x+w]
            cv2.imshow("Roi", imgRoi)


    cv2.imshow("Original", img)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("resources/scanned/NoPlate_"+str(count)+".jpg", imgRoi)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img,"scan Saved",(150,265),cv2.FONT_HERSHEY_DUPLEX,2,(0,0,255),2)
        cv2.imshow("Result", img)
        cv2.waitKey(500)
        count +=1
