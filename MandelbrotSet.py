import math
import numpy as np
import scipy.misc as smp
from PIL import PILLOW_VERSION
def iterate(x, y, iterationNum):
    z = 0
    coord = complex(x, y)
    while iterationNum:
        z = math.fabs(z * z) + coord
        if z ** 2 > 4:
            return False
    return True

def pixel(image,x,y,r,g,b):
   """Place pixel at pos=(x,y) on image, with color=(r,g,b)"""
   image.put("#%02x%02x%02x" % (r,g,b), (y, x))
def mandelbrot():
    WIDTH = 640; HEIGHT = 480
    TopLeftX = -200; BottomRightX = 200
    TopLeftY = 200; BottomRightY = -200
    Increment = 5
    maxIt = 100
    w = BottomRightX - TopLeftX
    h = TopLeftY - BottomRightY
    npArr = np.zeros((w / 0.05, h / 0.05, 3))
    for x in xrange(TopLeftX, BottomRightX, -5):
        for y in xrange(TopLeftY, BottomRightY, -5):
            xnum = x / 100.0
            ynum = y / 100.0
            if iterate(xnum, ynum, maxIt):
                npArr[xnum, ynum] == [0, 191, 255] # Changes it to blue
            else:
                npArr[xnum, ynum] == [255, 255, 255] # Changes color to white.
    return npArr

img = smp.toimage(mandelbrot())
img.save("mandelbrot.png")
