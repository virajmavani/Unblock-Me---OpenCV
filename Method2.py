import cv2
import numpy as np
import pyautogui as mouse
import math

cap = cv2.VideoCapture(0)

while(True):
	ret, frame = cap.read()
	frame = cv2.flip(frame,1)
	value = (35, 35)
	blurred = cv2.GaussianBlur(frame, value, 0)
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
	# imgray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	# print 'hsv:',hsv
	# cv2.imshow('hsv1',hsv)
	lower_skin = np.array([120,50,50])
	upper_skin = np.array([180,180,200])
	mask = cv2.inRange(hsv, lower_skin, upper_skin)
	# ret,mask = cv2.threshold(imgray,70,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
	cv2.imshow('mask',mask)
	# grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# value = (70, 255)
	# blurred = cv2.GaussianBlur(grey, value, 0)
	# _, thresh1 = cv2.threshold(grey, 70, 255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
	# cv2.imshow('Thresholded', thresh1)
  	
	image, contours, hierarchy = cv2.findContours(mask.copy(),cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	if contours == []:
		continue
	cnt = max(contours, key = lambda x: cv2.contourArea(x))
	
	x,y,w,h = cv2.boundingRect(cnt)
	cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
	centroid_x = (x + x+w)/2
	centroid_y = (y + y+h)/2
	cv2.circle(frame, (centroid_x, centroid_y), 2, (0,0,255), 2)
	hull = cv2.convexHull(cnt)
	# drawing = np.zeros(frame.shape,np.uint8)
	# cv2.drawContours(drawing,[cnt],0,(0,255,0),0)
	# cv2.drawContours(drawing,[hull],0,(0,0,255),0)
	# hull = cv2.convexHull(cnt,returnPoints = False)
	final_d = 480
	j=0
	d=hull.shape[0]		
	for i in range(0,d):
		v = hull[i][0][1]
		# dist = np.sqrt(np.power(hull[i][0][0]-centroid_x,2)+np.power(hull[i][0][1]-centroid_y,2))
		if v < final_d:
			final_d = v
			j=i
	
	cv2.circle(frame, (hull[j][0][0], hull[j][0][1]), 2, (0,0,255), 2)
	centroid_x = hull[j][0][0]
	centroid_y = hull[j][0][1]
	
	if centroid_x<=210 and centroid_y<=160:
			if centroid_x<=105 and centroid_y<=80:
				if move == 2:
					mouse.moveTo(360,190)
					# mouse.mouseDown()
					mouse.dragTo(320,190,button="left")
					# mouse.mouseUp()
				if move == 7:
					mouse.moveTo(320,230)
					mouse.dragTo(320,190,button="left")
				move = 1
			elif centroid_x>105 and centroid_y<=80:
				if move == 1:
					mouse.moveTo(320,190)
					mouse.dragTo(360,190,button="left")
				if move == 8:
					mouse.moveTo(360,230)
					mouse.dragTo(360,190,button="left")
				if move == 3:
					mouse.moveTo(400,190)
					mouse.dragTo(360,190,button="left")
				move = 2
			elif centroid_x<=105 and centroid_y>80:
				if move == 1:
					mouse.moveTo(320,190)
					mouse.dragTo(320,230,button="left")
				if move == 8:
					mouse.moveTo(360,230)
					mouse.dragTo(320,230,button="left")
				if move == 13:
					mouse.moveTo(320,275)
					mouse.dragTo(320,230,button="left")
				move = 7
			else:
				if move == 2:
					mouse.moveTo(360,190)
					mouse.dragTo(360,230,button="left")
				if move == 7:
					mouse.moveTo(320,230)
					mouse.dragTo(360,230,button="left")
				if move == 9:
					mouse.moveTo(400,230)
					mouse.dragTo(360,230,button="left")
				if move == 14:
					mouse.moveTo(360,275)
					mouse.dragTo(360,230,button="left")
				move = 8
		elif centroid_x<=420 and centroid_y<=160:
			if centroid_x<=315 and centroid_y<=80:
				if move == 2:
					mouse.moveTo(360,190)
					mouse.dragTo(400,190,button="left")
				if move == 4:
					mouse.moveTo(445,190)
					mouse.dragTo(400,190,button="left")
				if move == 9:
					mouse.moveTo(400,230)
					mouse.dragTo(400,190,button="left")
				move = 3
			elif centroid_x>315 and centroid_y<=80:
				if move == 3:
					mouse.moveTo(400,190)
					mouse.dragTo(445,190,button="left")
				if move == 5:
					mouse.moveTo(490,190)
					mouse.dragTo(445,190,button="left")
				if move == 10:
					mouse.moveTo(445,230)
					mouse.dragTo(445,190,button="left")
				move = 4
			elif centroid_x<=315 and centroid_y>80:
				if move == 3:
					mouse.moveTo(400,190)
					mouse.dragTo(400,230,button="left")
				if move == 8:
					mouse.moveTo(360,230)
					mouse.dragTo(400,230,button="left")
				if move == 10:
					mouse.moveTo(445,230)
					mouse.dragTo(400,230,button="left")
				if move == 15:
					mouse.moveTo(400,275)
					mouse.dragTo(400,230,button="left")
				move = 9
			else:
				if move == 4:
					mouse.moveTo(445,190)
					mouse.dragTo(445,230,button="left")
				if move == 9:
					mouse.moveTo(400,230)
					mouse.dragTo(445,230,button="left")
				if move == 11:
					mouse.moveTo(490,230)
					mouse.dragTo(445,230,button="left")
				if move == 16:
					mouse.moveTo(445,275)
					mouse.dragTo(445,230,button="left")
				move = 10
		elif centroid_x<=630 and centroid_y<=160:
			if centroid_x<=525 and centroid_y<=80:
				if move == 4:
					mouse.moveTo(445,190)
					mouse.dragTo(490,190,button="left")
				if move == 6:
					mouse.moveTo(530,190)
					mouse.dragTo(490,190,button="left")
				if move == 11:
					mouse.moveTo(490,230)
					mouse.dragTo(490,190,button="left")
				move = 5
			elif centroid_x>525 and centroid_y<=80:
				if move == 5:
					mouse.moveTo(490,190)
					mouse.dragTo(530,190,button="left")
				if move == 12:
					mouse.moveTo(530,230)
					mouse.dragTo(530,190,button="left")
				move = 6
			elif centroid_x<=525 and centroid_y>80:
				if move == 5:
					mouse.moveTo(490,190)
					mouse.dragTo(490,230,button="left")
				if move == 10:
					mouse.moveTo(445,230)
					mouse.dragTo(490,230,button="left")
				if move == 12:
					mouse.moveTo(530,230)
					mouse.dragTo(490,230,button="left")
				if move == 17:
					mouse.moveTo(490,275)
					mouse.dragTo(490,230,button="left")
				move = 11
			else:
				if move == 6:
					mouse.moveTo(530,190)
					mouse.dragTo(530,230,button="left")
				if move == 11:
					mouse.moveTo(490,230)
					mouse.dragTo(530,230,button="left")
				if move == 18:
					mouse.moveTo(530,275)
					mouse.dragTo(530,230,button="left")
				move = 12
		elif centroid_x<=210 and centroid_y<=320:
			if centroid_x<=105 and centroid_y<=240:
				if move == 7:
					mouse.moveTo(320,230)
					mouse.dragTo(320,275,button="left")
				if move == 14:
					mouse.moveTo(360,275)
					mouse.dragTo(320,275,button="left")
				if move == 19:
					mouse.moveTo(320,320)
					mouse.dragTo(320,275,button="left")
				move = 13
			elif centroid_x>105 and centroid_y<=240:
				if move == 8:
					mouse.moveTo(360,230)
					mouse.dragTo(360,275,button="left")
				if move == 13:
					mouse.moveTo(320,275)
					mouse.dragTo(360,275,button="left")
				if move == 15:
					mouse.moveTo(400,275)
					mouse.dragTo(360,275,button="left")
				if move == 20:
					mouse.moveTo(360,320)
					mouse.dragTo(360,275,button="left")
				move = 14
			elif centroid_x<=105 and centroid_y>240:
				if move == 13:
					mouse.moveTo(320,275)
					mouse.dragTo(320,320,button="left")
				if move == 20:
					mouse.moveTo(360,320)
					mouse.dragTo(320,320,button="left")
				if move == 25:
					mouse.moveTo(320,360)
					mouse.dragTo(320,320,button="left")
				move = 19
			else:
				if move == 14:
					mouse.moveTo(360,275)
					mouse.dragTo(360,320,button="left")
				if move == 19:
					mouse.moveTo(320,320)
					mouse.dragTo(360,320,button="left")
				if move == 21:
					mouse.moveTo(400,320)
					mouse.dragTo(360,320,button="left")
				if move == 26:
					mouse.moveTo(360,360)
					mouse.dragTo(360,320,button="left")
				move = 20
		elif centroid_x<=420 and centroid_y<=320:
			if centroid_x<=315 and centroid_y<=240:
				if move == 9:
					mouse.moveTo(400,230)
					mouse.dragTo(400,275,button="left")
				if move == 14:
					mouse.moveTo(360,275)
					mouse.dragTo(400,275,button="left")
				if move == 16:
					mouse.moveTo(445,275)
					mouse.dragTo(400,275,button="left")
				if move == 21:
					mouse.moveTo(400,320)
					mouse.dragTo(400,275,button="left")
				move = 15
			elif centroid_x>315 and centroid_y<=240:
				if move == 10:
					mouse.moveTo(445,230)
					mouse.dragTo(445,275,button="left")
				if move == 15:
					mouse.moveTo(400,275)
					mouse.dragTo(445,275,button="left")
				if move == 17:
					mouse.moveTo(490,275)
					mouse.dragTo(445,275,button="left")
				if move == 22:
					mouse.moveTo(445,320)
					mouse.dragTo(445,275,button="left")
				move = 16
			elif centroid_x<=315 and centroid_y>240:
				if move == 15:
					mouse.moveTo(400,275)
					mouse.dragTo(400,320,button="left")
				if move == 20:
					mouse.moveTo(360,320)
					mouse.dragTo(400,320,button="left")
				if move == 22:
					mouse.moveTo(445,320)
					mouse.dragTo(400,320,button="left")
				if move == 27:
					mouse.moveTo(400,360)
					mouse.dragTo(400,320,button="left")
				move = 21
			else:
				if move == 16:
					mouse.moveTo(445,275)
					mouse.dragTo(445,320,button="left")
				if move == 21:
					mouse.moveTo(400,320)
					mouse.dragTo(445,320,button="left")
				if move == 23:
					mouse.moveTo(490,320)
					mouse.dragTo(445,320,button="left")
				if move == 28:
					mouse.moveTo(445,360)
					mouse.dragTo(445,320,button="left")
				move = 22
		elif centroid_x<=630 and centroid_y<=320:
			if centroid_x<=525 and centroid_y<=240:
				if move == 11:
					mouse.moveTo(490,230)
					mouse.dragTo(490,275,button="left")
				if move == 16:
					mouse.moveTo(445,275)
					mouse.dragTo(490,275,button="left")
				if move == 18:
					mouse.moveTo(530,275)
					mouse.dragTo(490,275,button="left")
				if move == 23:
					mouse.moveTo(490,320)
					mouse.dragTo(490,275,button="left")
				move = 17
			elif centroid_x>525 and centroid_y<=240:
				if move == 12:
					mouse.moveTo(530,230)
					mouse.dragTo(530,275,button="left")
				if move == 17:
					mouse.moveTo(490,275)
					mouse.dragTo(530,275,button="left")
				if move == 24:
					mouse.moveTo(530,320)
					mouse.dragTo(530,275,button="left")
				move = 18
			elif centroid_x<=525 and centroid_y>240:
				if move == 17:
					mouse.moveTo(490,275)
					mouse.dragTo(490,320,button="left")
				if move == 22:
					mouse.moveTo(445,320)
					mouse.dragTo(490,320,button="left")
				if move == 24:
					mouse.moveTo(530,320)
					mouse.dragTo(490,320,button="left")
				if move == 29:
					mouse.moveTo(490,360)
					mouse.dragTo(490,320,button="left")
				move = 23
			else:
				if move == 18:
					mouse.moveTo(530,275)
					mouse.dragTo(530,320,button="left")
				if move == 23:
					mouse.moveTo(490,320)
					mouse.dragTo(530,320,button="left")
				if move == 30:
					mouse.moveTo(530,360)
					mouse.dragTo(530,320,button="left")
				move = 24
		elif centroid_x<=210 and centroid_y<=480:
			if centroid_x<=105 and centroid_y<=400:
				if move == 19:
					mouse.moveTo(320,320)
					mouse.dragTo(320,360,button="left")
				if move == 26:
					mouse.moveTo(360,360)
					mouse.dragTo(320,360,button="left")
				if move == 31:
					mouse.moveTo(320,405)
					mouse.dragTo(320,360,button="left")
				move = 25
			elif centroid_x>105 and centroid_y<=400:
				if move == 20:
					mouse.moveTo(360,320)
					mouse.dragTo(360,360,button="left")
				if move == 25:
					mouse.moveTo(320,360)
					mouse.dragTo(360,360,button="left")
				if move == 27:
					mouse.moveTo(400,360)
					mouse.dragTo(360,360,button="left")
				if move == 32:
					mouse.moveTo(360,405)
					mouse.dragTo(360,360,button="left")
				move = 26
			elif centroid_x<=105 and centroid_y>400:
				if move == 25:
					mouse.moveTo(320,360)
					mouse.dragTo(320,405,button="left")
				if move == 32:
					mouse.moveTo(360,405)
					mouse.dragTo(320,405,button="left")
				move = 31
			else:
				if move == 26:
					mouse.moveTo(360,360)
					mouse.dragTo(360,405,button="left")
				if move == 31:
					mouse.moveTo(320,405)
					mouse.dragTo(360,405,button="left")
				if move == 33:
					mouse.moveTo(400,405)
					mouse.dragTo(360,405,button="left")
				move = 32
		elif centroid_x<=420 and centroid_y<=480:
			if centroid_x<=315 and centroid_y<=400:
				if move == 21:
					mouse.moveTo(400,320)
					mouse.dragTo(400,360,button="left")
				if move == 26:
					mouse.moveTo(360,360)
					mouse.dragTo(400,360,button="left")
				if move == 28:
					mouse.moveTo(445,360)
					mouse.dragTo(400,360,button="left")
				if move == 33:
					mouse.moveTo(400,405)
					mouse.dragTo(400,360,button="left")
				move = 27
			elif centroid_x>315 and centroid_y<=400:
				if move == 22:
					mouse.moveTo(445,320)
					mouse.dragTo(445,360,button="left")
				if move == 27:
					mouse.moveTo(400,360)
					mouse.dragTo(445,360,button="left")
				if move == 29:
					mouse.moveTo(490,360)
					mouse.dragTo(445,360,button="left")
				if move == 34:
					mouse.moveTo(445,405)
					mouse.dragTo(445,360,button="left")
				move = 28
			elif centroid_x<=315 and centroid_y>400:
				if move == 27:
					mouse.moveTo(400,360)
					mouse.dragTo(400,405,button="left")
				if move == 32:
					mouse.moveTo(360,405)
					mouse.dragTo(400,405,button="left")
				if move == 34:
					mouse.moveTo(445,405)
					mouse.dragTo(400,405,button="left")
				move = 33
			else:
				if move == 28:
					mouse.moveTo(445,360)
					mouse.dragTo(445,405,button="left")
				if move == 33:
					mouse.moveTo(400,405)
					mouse.dragTo(445,405,button="left")
				if move == 35:
					mouse.moveTo(490,405)
					mouse.dragTo(445,405,button="left")
				move = 34
		elif centroid_x<=630 and centroid_y<=480:
			if centroid_x<=525 and centroid_y<=400:
				if move == 23:
					mouse.moveTo(490,320)
					mouse.dragTo(490,360,button="left")
				if move == 28:
					mouse.moveTo(445,360)
					mouse.dragTo(490,360,button="left")
				if move == 30:
					mouse.moveTo(530,360)
					mouse.dragTo(490,360,button="left")
				if move == 35:
					mouse.moveTo(490,405)
					mouse.dragTo(490,360,button="left")
				move = 29
			elif centroid_x>525 and centroid_y<=400:
				if move == 24:
					mouse.moveTo(530,320)
					mouse.dragTo(530,360,button="left")
				if move == 29:
					mouse.moveTo(490,360)
					mouse.dragTo(530,360,button="left")
				if move == 36:
					mouse.moveTo(530,405)
					mouse.dragTo(530,360,button="left")
				move = 30
			elif centroid_x<=525 and centroid_y>400:
				if move == 29:
					mouse.moveTo(490,360)
					mouse.dragTo(490,405,button="left")
				if move == 34:
					mouse.moveTo(445,405)
					mouse.dragTo(490,405,button="left")
				if move == 36:
					mouse.moveTo(530,405)
					mouse.dragTo(490,405,button="left")
				move = 35
			else:
				if move == 30:
					mouse.moveTo(530,360)
					mouse.dragTo(530,405,button="left")
				if move == 35:
					mouse.moveTo(490,405)
					mouse.dragTo(530,405,button="left")
				move = 36
	
	print "Move:", move
	
	cv2.rectangle(frame,(0,0),(105,80),(0,0,0))
	cv2.rectangle(frame,(106,0),(210,80),(0,0,0))
	cv2.rectangle(frame,(211,0),(315,80),(0,0,0))
	cv2.rectangle(frame,(316,0),(420,80),(0,0,0))
	cv2.rectangle(frame,(421,0),(525,80),(0,0,0))
	cv2.rectangle(frame,(526,0),(630,80),(0,0,0))
	cv2.rectangle(frame,(0,81),(105,160),(0,0,0))
	cv2.rectangle(frame,(106,81),(210,160),(0,0,0))
	cv2.rectangle(frame,(211,81),(315,160),(0,0,0))
	cv2.rectangle(frame,(316,81),(420,160),(0,0,0))
	cv2.rectangle(frame,(421,81),(525,160),(0,0,0))
	cv2.rectangle(frame,(526,81),(630,160),(0,0,0))
	cv2.rectangle(frame,(0,161),(105,240),(0,0,0))
	cv2.rectangle(frame,(106,161),(210,240),(0,0,0))
	cv2.rectangle(frame,(211,161),(315,240),(0,0,0))
	cv2.rectangle(frame,(316,161),(420,240),(0,0,0))
	cv2.rectangle(frame,(421,161),(525,240),(0,0,0))
	cv2.rectangle(frame,(526,161),(630,240),(0,0,0))
	cv2.rectangle(frame,(0,241),(105,320),(0,0,0))
	cv2.rectangle(frame,(106,241),(210,320),(0,0,0))
	cv2.rectangle(frame,(211,241),(315,320),(0,0,0))
	cv2.rectangle(frame,(316,241),(420,320),(0,0,0))
	cv2.rectangle(frame,(421,241),(525,320),(0,0,0))
	cv2.rectangle(frame,(526,241),(630,320),(0,0,0))
	cv2.rectangle(frame,(0,321),(105,400),(0,0,0))
	cv2.rectangle(frame,(106,321),(210,400),(0,0,0))
	cv2.rectangle(frame,(211,321),(315,400),(0,0,0))
	cv2.rectangle(frame,(316,321),(420,400),(0,0,0))
	cv2.rectangle(frame,(421,321),(525,400),(0,0,0))
	cv2.rectangle(frame,(526,321),(630,400),(0,0,0))
	cv2.rectangle(frame,(0,401),(105,480),(0,0,0))
	cv2.rectangle(frame,(106,401),(210,480),(0,0,0))
	cv2.rectangle(frame,(211,401),(315,480),(0,0,0))
	cv2.rectangle(frame,(316,401),(420,480),(0,0,0))
	cv2.rectangle(frame,(421,401),(525,480),(0,0,0))
	cv2.rectangle(frame,(526,401),(630,480),(0,0,0))
	
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cap.destroyAllWindows()
