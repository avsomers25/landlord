import cv2
import numpy as np
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('test.png')
roi = img[40:140,190:600]

barroi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
scale_percent = 100 # percent of original size
width = int(barroi.shape[1] * scale_percent / 100)
height = int(barroi.shape[0] * scale_percent / 100)
dim = (width, height)
barroi = cv2.resize(barroi, dim, interpolation = cv2.INTER_AREA)

barroi = cv2.GaussianBlur(barroi,(5,5),0)
barroi = cv2.medianBlur(barroi, 5)
barroi = cv2.GaussianBlur(barroi,(5,5),0)
#barroi = cv2.medianBlur(barroi, 5)
#barroi = cv2.GaussianBlur(barroi,(5,5),0)
#barroi = cv2.medianBlur(barroi, 5)
#barroi = cv2.GaussianBlur(barroi,(5,5),0)
#barroi = cv2.medianBlur(barroi, 5)
kernel = np.ones((3,3),np.uint8)
barroi = cv2.erode(barroi,kernel,iterations = 1)

(thresh, barroi) = cv2.threshold(barroi, 0, 255, cv2.THRESH_OTSU | 
cv2.THRESH_BINARY)
cv2.imwrite("testing.tif", barroi)

cv2.imshow("Display window", barroi)
k = cv2.waitKey(0)

text = pytesseract.image_to_string(barroi, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
print(" "+str(text))

'''
imageName =  "Region"+str(region)+".tif"
cv2.imwrite(imageName, roi)

cv2.putText(img, "Result: "+str(text), ROIRegion[region][0], 
cv2.FONT_HERSHEY_SIMPLEX , 0.7, (255,0,0), 2)
imageName =  "Result.tif"
cv2.imwrite(imageName, img)
cv2.namedWindow('Result')
cv2.imshow('Result',img)
'''