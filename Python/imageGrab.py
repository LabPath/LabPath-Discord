from PIL import ImageGrab, Image
import win32gui
import sys
import pytesseract
import argparse
import cv2
import os

toplist, winlist = [], []
platform = sys.platform # will want to expand this so we can program around the different OSes. Currently this script is only Windows.

def enum_cb(hwnd, results):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))


def rgbToHex(rgb):
    return '%02x%02x%02x' % rgb


def hexToRGB(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))


win32gui.EnumWindows(enum_cb, toplist)

bluestacks = [(hwnd, title)
for hwnd, title in winlist if 'bluestacks' in title.lower()]
# just grab the hwnd for first window matching bluestacks
bluestacks = bluestacks[0]
hwnd = bluestacks[0]

win32gui.SetForegroundWindow(hwnd)
bbox = win32gui.GetWindowRect(hwnd)
img = ImageGrab.grab(bbox)
# img.show()
print(bbox)
testPixel = img.getpixel((285, 336))

# going to need to scale the image to 1920x1080, 16:9 ratio This allows us to conform to a single size, so we can operate within those parameters without having to significantly worry about the differences



testHex = rgbToHex((testPixel))
print(testHex)
path = "D:\\Users\\jreiber\\Desktop\\test.png"
img.save(path)

text = pytesseract.image_to_string(Image.open(path))
os.remove(path)
print(text)
