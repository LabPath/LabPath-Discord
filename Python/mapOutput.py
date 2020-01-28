import turtle
import time
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

# each side of the hexagon should be about 32 pixels. Makes the Height/width 64px
# 24 hexagons total in horizontal rows in this pattern: 1, 2, 3, 2, 3, 2, 3, 2, 3, 2, 1
# original has the start hex of each floor 204px away. probably going to make it either 192 or 224 to standardize on multiples of 32
# starting angle needs to be either 90 or 270 to properly orient the drawn hexagon
# might need to setup the draw function to take an arg for direction: BL, BR, TL, TR
# may need a function for shifting over one hexagon

# Drawing the outside: LRLRLRRLLRRLLRRLLRRLRLRRRLRLRRLLRRLLRRLLRRLRLR


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
