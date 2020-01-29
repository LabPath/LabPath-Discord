import turtle
import time
import json

t = turtle.Turtle()
bFlag = "#C9A7A7"
rFlag = "#F01B20"
boss = "#FEC90A"
wagon = "#252E87"
fountain = "#9AD7EB"
res = "#FE3DBB"
wrizz = "#000000"
start = "#FFFFFF"

#Trying to be able to draw the map with Python. Will also be recording some information on the specifics of the picture for reference.
# As far as I can tell, this should function at the very least on Python 3.6+. Written in Python 3.8.1

# each side of the hexagon should be about 32 pixels. Makes the Height 64px and width of about 55.43 (side^2+width^2=height^2)
# 24 hexagons total in horizontal rows in this pattern: 1, 2, 3, 2, 3, 2, 3, 2, 3, 2, 1
# original has the start hex of each floor 204px away. probably going to make it either 192 or 224 to standardize on multiples of 32
# starting angle needs to be either 90 or 270 to properly orient the drawn hexagon
# might need to setup the draw function to take an arg for direction: BL, BR, TL, TR
# may need a function for shifting over one hexagon

# Drawing the outside: LRLRLRRLLRRLLRRLLRRLRLRRRLRLRRLLRRLLRRLLRRLRLR

# may need or want to have a variable for each spot. a1-d24, a-d being floors, 1-24 being location on that floor.
#   better idea, use a nested dictionary. Can be printed in JSON, so perfect place to store the map key.
#   To print it to JSON:
#     app_json = json.dumps(mapKey, sort_keys=True)
#   mapKey = { '1': { '1':'Start','24':'Boss'},'2': {'1':'Start','24':'Boss'},'3': {'1':'Start','24':'Boss'},'Hardmode': {'1':'Start','24':'Boss'}}
# Mapping Origins of Hexagons:
#   Hexagons are numbered bottom-to-top, left-to-right. Origin is bottom point of each hexagon
#   1: (0,0)
#   2: (-27.71,48.00)
#   3: (27.71,48.00)
#   4: (-55.43,96.00)
#   5: (0.00,96.00)

# 1,5,10,15,20,24 are all going to have a 0.00 x-value. Y-value increases by 96 each step, with 24 being (0.00,480)

def drawHex():
  for i in range(6):
    t.right(60)  # Turning the turtle by 60 degree
    t.forward(32)  # Each side is 32px long

def leftForward():
  t.left(60)
  t.forward(32)

def rightForward():
  t.right(60)
  t.forward(32)

def drawOutside():
  directions = "LRLRLRRLLRRLLRRLLRRLRLRRRLRLRRLLRRLLRRLLRRLRLR"
  dLen = len(directions)
  t.left(90)
  for n in range(dLen):
    if directions[n] == "L":
      leftForward()
    elif directions[n] == "R":
      rightForward()

# a1 = "start"
# t.goto(x, y)  It moves the turtle(arrow) to the position x, y


def testingHexes():
  t.left(90)
  # t.fillcolor(res)
  t.fillcolor(fountain)
  t.begin_fill()
  drawHex()
  t.end_fill()
  t.left(120)
  t.fillcolor(res)
  t.begin_fill()
  drawHex()
  t.end_fill()
  t.back(32)
  t.right(60)
  t.fillcolor(bFlag)
  t.begin_fill()
  drawHex()
  t.end_fill()
# drawOutside()
testingHexes()
time.sleep(3)
