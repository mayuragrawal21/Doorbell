# importing the python open cv library
import cv2
import telepot
from datetime import datetime
bot = telepot.Bot('5717459496:AAGJ8fG4xyR8ZNttAZdnBrIb9dAfZ0iSLeg')
date_time_now = datetime.now()
date_time = date_time_now.strftime("%d/%m/%Y %H:%M:%S")
# intialize the webcam and pass a constant which is 0
cam = cv2.VideoCapture(0)
# title of the app
cv2.namedWindow('python webcam screenshot app')
# let's assume the number of images gotten is 0
img_counter = 0
# while loop
while True:
    # intializing the frame, ret
    ret, frame = cam.read()
    # if statement
    if not ret:
        print('failed to grab frame')
        break
    # the frame will show with the title of test
    cv2.imshow('test', frame)
    #to get continuous live video feed from my laptops webcam
    k  = cv2.waitKey(1)
    # if the escape key is been pressed, the app will stop
    if k%256 == 27:
        print('escape hit, closing the app')
        break
    # if the spacebar key is been pressed
    # screenshots will be taken
    elif k%256  == 32:
        # the format for storing the images scrreenshotted
        img_name = f'opencv_frame_{img_counter}'
        # saves the image as a png file
        cv2.imwrite("filename.jpg", frame)
        print('screenshot taken')
        # here replace chat_id and test.jpg with real things
        bot.sendPhoto('946594421', photo=open('filename.jpg', 'rb'), caption = date_time)
        
        # the number of images automaticallly increases by 1
        img_counter += 1
# release the camera
cam.release()
# stops the camera window
cam.destoryAllWindows()