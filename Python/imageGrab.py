from PIL import ImageGrab, Image # Pillow
import win32gui # pywin32
import sys
import pytesseract # pytesseract
import argparse
import cv2 # opencv-python
import os


# refs:
#   - Pixel Color Count: https://github.com/townsean/pixel-color-count/blob/master/pixel-color-count.py
#bluestacks top right: 3340,0,3840,940
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


def count_pixels(crop):
  color_count = {}
  color_count["nonText"] = 0
  color_count["Text"] = 0
  sum = 0
  with crop as image:
    width, height = image.size
    rgb_image = image.convert('RGB')
    # iterate through each pixel in the image and keep a count per unique color
    for x in range(width):
      for y in range(height):
        sum = 0
        rgb = rgb_image.getpixel((x, y))
        for val in rgb:
          sum += val
        if sum < 250:
          color_count["nonText"] += 1 # not text
        else:
          color_count["Text"] += 1 # is text
        if rgb in color_count:
          color_count[rgb] += 1
        else:
          color_count[rgb] = 1
  return color_count


win32gui.EnumWindows(enum_cb, toplist)

bluestacks = [(hwnd, title)
for hwnd, title in winlist if 'bluestacks' in title.lower()]
# just grab the hwnd for first window matching bluestacks
bluestacks = bluestacks[0]
hwnd = bluestacks[0]

win32gui.SetForegroundWindow(hwnd)
bbox = win32gui.GetWindowRect(hwnd)
img = ImageGrab.grab(bbox)
#img.show()
#print(bbox)
#testPixel = img.getpixel((285, 336))

# going to need to scale the image to 1920x1080, 16:9 ratio This allows us to conform to a single size, so we can operate within those parameters without having to significantly worry about the differences

# 60,817 ref point for screen?
# 248,735 for flag at 0
# 140,60 - start of location banner .28
# 360,78 - end of location banner .72
# bluestacks banner is .045 of height
# Without bluestacks banner is X(.28,.72),Y(.019,.035) total approx 500,926
# With, Y(.064.085)
# X(.04,84)
# Y values of the columns of platforms
# 115,180,250,320,380
pctFloorName = {}
pctFloorName["x1"] = 0.28055555555555556
pctFloorName["x2"] = 0.7212962962962963
pctFloorName["y1"] = 0.014864864864864866
pctFloorName["y2"] = 0.034684684684684684
x1 = int(img.size[0]*pctFloorName["x1"])
x2 = int(img.size[0]*pctFloorName["x2"])
y1 = int(img.size[1]*pctFloorName["y1"])
y2 = int(img.size[1]*pctFloorName["y2"])
crop = img.crop((x1,y1,x2,y2))
#crop.show()
# X range for main screen:
#   115-790 130-820
# --Depends on Bluestacks Banner
cnt = count_pixels(crop)
pctFloor = {}
pctChk = {}
pctBanners = {}
pctBanners["Top"] = 0.05855855855855856
pctBanners["Bottom"] = 0.10045045045045045
pctFloor["Hardmode"] = 0.39055222887558216
pctFloor["Floor1"] = 0.3136392206159648
pctFloor["Floor3"] = 0.3244613434727503
pctChk["FloorCheck"] = cnt["Text"] / cnt["nonText"]
color_count = count_pixels(crop)
for flr,pct in pctFloor.items():
  if pctChk["FloorCheck"] == pct:
    #return flr
    floor = flr

color_index=1
for color, count in color_count.items():
  try:
    color_name = webcolors.rgb_to_name(color)
  except ValueError:
    color_name = color
  print('{}.) {}: {}'.format(color_index, color_name, count))
  color_index += 1

for color, count in color_count.items():
  if count <= 75:
    continue
  else:
    print(color,count)


print('-' * 30)
print('\t{} pixels'.format(sum(color_count[color] for color in color_count)))
# Hard mode: {'nonText': 3006, 'Text': 1174}
# floor 3: {'nonText': 3156, 'Text': 1024}
# floor 1: {'nonText': 3182, 'Text': 998}
# platforms start at x:56 and end at x:443
#   - 56(left)
#   - each platform is 120px wide
#   - 66/67px between centers
#   - 13/14px padding
# approx(?) .11 off of each side
# MagicNum = 0.13518518518518519
#  ( width / 2 ) + ( ( width * magicnum ) * offset ) will give you the x-value of the centerline of column 2, which would be the first platform in the 2-set.
# testHex = rgbToHex((testPixel))
# print(testHex)
path = "C:\\Users\\joejo\\Downloads\\test.png"
img.save(path)
print(pytesseract.image_to_string(img))
# text = pytesseract.image_to_string(Image.open(path))
# os.remove(path)
# print(text)
