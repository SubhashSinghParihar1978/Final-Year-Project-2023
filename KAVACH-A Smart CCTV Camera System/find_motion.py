import cv2
from spot_diff import spot_diff
import time

def find_motion():

	motion_detected = False
	is_start_done = False

	cap = cv2.VideoCapture(0)
	
	print("waiting for 2 seconds")
	time.sleep(2)
	frame1 = cap.read()

	_, frm1 = cap.read()
	frm1 = cv2.cvtColor(frm1, cv2.COLOR_BGR2GRAY)

	while True:
		_, frm2 = cap.read()
		# used to convert an image from one color space to other
		frm2 = cv2.cvtColor(frm2, cv2.COLOR_BGR2GRAY)

		# finds the difference between the two frames
		diff = cv2.absdiff(frm1, frm2)

		# creating a binary img from grayscale img - img/scalevalues(if 30> , to 255)/
		_, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

		# works best on bin img , retrives external contours , removes all redundant points and compresses contour
		contors = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

		#look at the objects that are stored previously via findContours
		contors = [c for c in contors if cv2.contourArea(c) > 25]

		if len(contors) > 5:
			cv2.putText(thresh, "motion detected", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
			motion_detected = True
			is_start_done = False
		# elif motion_detected and
		elif motion_detected and len(contors) < 3:
			if (is_start_done) == False:
				start = time.time()
				is_start_done = True
				# end = time.time()

			# start = time.time()
			end = time.time()

			if (end - start) > 4:
				frame2 = cap.read()
				cap.release()
				cv2.destroyAllWindows()
				x = spot_diff(frame1, frame2)

				if x == 0:
					print("Running Again")
					return

				else:
					print("Found motion")
					return

		else:
			cv2.putText(thresh, "No motion detected", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)

		cv2.imshow("motion", thresh)

		_, frm1 = cap.read()
		frm1 = cv2.cvtColor(frm1, cv2.COLOR_BGR2GRAY)

		if cv2.waitKey(1) == 27:
			break

	return