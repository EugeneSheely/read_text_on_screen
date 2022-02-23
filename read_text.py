from PIL import Image
from pytesseract import pytesseract #pip install pytesseract https://github.com/UB-Mannheim/tesseract/wiki
# there's additional languages download i need to select: https://www.youtube.com/watch?v=RewxjHw8310
from pyautogui import *
import pyautogui
import time
import keyboard
# Defining paths to tesseract.exe
# and the image we would be using
path_to_tesseract = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"



while keyboard.is_pressed('q') == False:



    # image image:
    """im1 = pyautogui.screenshot()  # return an image object
    im2 = pyautogui.screenshot('my_screenshot.png')  # image name will be as per parameter
    im3 = pyautogui.screenshot(region=(0, 0, 300, 400))  # mention spedific region to get the screenshot

    im1.size()  # will return a dimension of image as a tuple
    im2.save(r"img.png")  # save the image
    im.getpixel((100, 200))  # return color value of the point mentioned"""

    im1 = pyautogui.screenshot(region=(0,0, 300, 400))
    im1.save(r"img.png")
    image_path = r"img.png"





    # Opening the image & storing it in an image object
    img = Image.open(image_path)

    # Providing the tesseract executable
    # location to pytesseract library
    pytesseract.tesseract_cmd = path_to_tesseract

    # Passing the image object to image_to_string() function
    # This function will extract the text from the image
    text = pytesseract.image_to_string(img)

    # Displaying the extracted text
    print(text[:-1])
    time.sleep(10)
