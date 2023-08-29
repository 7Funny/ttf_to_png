import cv2
import svgwrite


image = cv2.imread('result0/Elem.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh_image = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
approx_contours = cv2.approxPolyDP(contours[0], 0.01 * cv2.arcLength(contours[0], True), True)

drawing = svgwrite.Drawing('result0/newfile.svg', profile='full')
polyline = drawing.add(drawing.polyline(points=approx_contours[:,0,:]))
polyline.stroke('red', width=1, opacity=1, linecap='round')
polyline.fill('none').drawing.add(polyline)
drawing.save()