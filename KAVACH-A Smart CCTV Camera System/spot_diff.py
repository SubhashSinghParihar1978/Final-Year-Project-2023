import cv2
from skimage.metrics import structural_similarity
from pygame import mixer
import time
import threading
from datetime import datetime
def play_alarm_sound_function():

    mixer.init()  # Initialzing pyamge mixer
    mixer.music.load('alarm.mp3')  # Loading Music File
    mixer.music.play()  # Playing Music with Pygame
    time.sleep(5)
    mixer.music.stop()

def spot_diff(frame1, frame2):

	frame1 = frame1[1]
	frame2 = frame2[1]

	g1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
	g2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

	# To protect from any sudden change in intensity , smoothens the edges
	g1 = cv2.blur(g1, (2,2))
	g2 = cv2.blur(g2, (2,2))

	# Checks for quality check of compressed image - score has been shown (0.9 and above) is good
	(score, diff) = structural_similarity(g2, g1, full=True)

	print("Image similarity", score)

	diff = (diff * 255).astype("uint8")

	# Binarization of an image
	thresh = cv2.threshold(diff, 100, 255, cv2.THRESH_BINARY_INV)[1]

	# works best on bin img , retrives external contours , removes all redundant points and compresses contour
	contors = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
	contors = [c for c in contors if cv2.contourArea(c) > 100]

	if len(contors):
		for c in contors:
		
			x,y,w,h = cv2.boundingRect(c)

			cv2.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)	

	else:
		print("Nothing Stolen")
		return False

	cv2.imshow("diff", thresh)
	threading.Thread(target=play_alarm_sound_function).start()
	cv2.imshow("win1", frame1)
	# Change
	cv2.imwrite(f'Watch/stolen/thing10.jpg', frame1)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	return True