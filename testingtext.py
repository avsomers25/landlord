import cv2 as cv
import numpy as np
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def gray_and_tesseract(img, number):
    invert = cv.bitwise_not(img)
    invert_gray = cv.cvtColor(invert, cv.COLOR_BGR2GRAY)

    if(number):     
        kernel = np.ones((5,5),np.float32)/25
        invert_gray = cv.filter2D(invert_gray, -1, kernel)

    

    cv.imshow("Display window", invert_gray)
    k = cv.waitKey(0)

    text = pytesseract.image_to_string(invert_gray)

    return text





def name_symbols(img):
    # 1 x cords = 375:750
    # 2 x cords = 770:1150
    # 3 x cords = 1165:1540

    print(gray_and_tesseract(img[325:400,375:750], False))
    print(gray_and_tesseract(img[325:400, 770:1150], False))
    print(gray_and_tesseract(img[325:400, 1165:1540], False))


def coins(img):

    print(gray_and_tesseract(img[40:140,690:800], True))
    print(gray_and_tesseract(img[40:140,200:600], True))



  





img = cv.imread('test.png')
print(img.shape)

coins(img)
name_symbols(img)
