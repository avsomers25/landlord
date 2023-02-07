import cv2 
import numpy as np
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def gray_and_tesseract(img):
    invert = cv2.bitwise_not(img)
    invert_gray = cv2.cvtColor(invert, cv2.COLOR_BGR2GRAY)
    invert_gray = cv2.threshold(invert_gray, 0,255,cv2.THRESH_BINARY| cv2.THRESH_OTSU)[1]

    invert_gray = cv2.medianBlur(invert_gray, 5)

    cv2.imshow("Display window", invert_gray)
    k = cv2.waitKey(0)

    text = pytesseract.image_to_string(invert_gray, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvqxyz.-')

    return text





def name_symbols(img):
    # 1 x cords = 375:750
    # 2 x cords = 770:1150
    # 3 x cords = 1165:1540

    print(gray_and_tesseract(img[325:400,375:750]))
    print(gray_and_tesseract(img[325:400, 770:1150]))
    print(gray_and_tesseract(img[325:400, 1165:1540]))


def coins(img):
    print(gray_and_tesseract(img[40:140,690:800]))
    print(gray_and_tesseract(img[40:140,200:600]))




for i in range(1 ,18):
    print(i)
    img = cv2.imread('test_' + str(i) + '.png')
    print(img.shape)
    name_symbols(img)


