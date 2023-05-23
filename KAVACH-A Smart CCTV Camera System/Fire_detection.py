import cv2
import threading
import numpy as np
import pywhatkit
from pygame import mixer
import time
from datetime import datetime, timedelta

def play_alarm_sound_function():

    mixer.init()  # Initialzing pyamge mixer
    mixer.music.load('alarm.mp3')  # Loading Music File
    mixer.music.play()  # Playing Music with Pygame
    time.sleep(5)
    mixer.music.stop()


def send_mail_function():

    now = datetime.now()
    currentime = now + timedelta(minutes=2)
    hours = int(currentime.strftime('%H'))
    minutes = int(currentime.strftime('%M'))
    seconds = int(currentime.strftime('%S'))
    pywhatkit.sendwhatmsg('+918127683667', 'Alert!!! Fire in the house.', hours, minutes,seconds)

 # If you want to use webcam use Index like 0,1.
Alarm_Status = False
Email_Status = False
Fire_Reported = 0
def find_fire():
    video = cv2.VideoCapture(0)
    while True:
        (grabbed, frame) = video.read()
        if not grabbed:

            break

        frame = cv2.resize(frame, (960, 540))

        blur = cv2.GaussianBlur(frame, (21, 21), 0)
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

        lower = [18, 50, 50]
        upper = [35, 255, 255]
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        mask = cv2.inRange(hsv, lower, upper)

        output = cv2.bitwise_and(frame, hsv, mask=mask)

        no_red = cv2.countNonZero(mask)

        if int(no_red) > 15000:
            global Fire_Reported
            Fire_Reported = Fire_Reported + 1
            if Fire_Reported >= 1:

                global Alarm_Status
                if Alarm_Status == False:
                    threading.Thread(target=play_alarm_sound_function).start()
                    Alarm_Status = True
                # Change
                path = f'fire_images/fires/203.jpg'
                cv2.imwrite(path, frame)
                global Email_Status
                if Email_Status == False:
                    threading.Thread(target=send_mail_function).start()

                    Email_Status = True

        cv2.imshow("output", output)
        # cv2.imshow("Press q to exit",frame)
        if grabbed == False:
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    video.release()
