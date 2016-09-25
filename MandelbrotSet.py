import math
import numpy as np
import scipy.misc as smp
from PIL import PILLOW_VERSION
from PIL import Image

def iterate(x, y, iterationNum):
    z = 0
    coord = complex(x, y)
    for a in xrange(iterationNum):
        z = z * z + coord
        if abs(z) > 2:
            return False
    return True

def draw(grid):
    img = Image.new('RGB', (len(grid), len(grid)), "white")
    pixels = img.load()
    for row in xrange(len(grid)):
        for col in xrange(len(grid[row])):
            if grid[row][col] == True:
                pixels[row, col] = (0, 0, 255)
    return img

def mandelbrot():
    TopLeftX = -2; BottomRightX = 2
    TopLeftY = 2; BottomRightY = -2
    increment = 0.01
    maxIt = 100
    w = BottomRightX - TopLeftX
    h = TopLeftY - BottomRightY
    #You needed to make sure these are ints!
    #Can't create an array with decimal size
    npArr = np.zeros((int(w / increment), int(h / increment)), dtype=bool)
    #Use the increment variable from above. It won't work with xrange because that doesn't
    #Support decimals. You probably want to use a while loop or something
    x = -2
    y = 2
    count = 0
    while TopLeftX <= x <= BottomRightX:
        y = 2
        while TopLeftY >= y >= BottomRightY:
            if iterate(x, y, maxIt):
                #So this is where the biggest issue is...
                #Your x is going to be between -2 and 2 (as a decimal)
                #But the array has values between 0 and w / increment
                #So we need to convert back to the npArr coordinate system
                
                #This is what you had:
                #npArr[x][y] = True
                
                #This is what it should be:
                npArr[int((x - TopLeftX) / increment)][int((y - BottomRightY) / increment)] = True
                #Think of it this way... TopLeftX should be 0 in the array and BottomLeftX should be w / increment
                #So to convert them, take x - TopLeftX and then expand it to be the size of the array (/ increment)
                count += 1
            y -= increment
        x += increment
    return npArr

img = draw(mandelbrot())
img.save("mandelbrot.png")
