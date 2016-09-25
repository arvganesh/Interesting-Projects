import math
import numpy as np
import scipy.misc as smp
from PIL import PILLOW_VERSION
from PIL import Image

def iterate(x, y, iterationNum):
    z = 0
    coord = complex(x, y)
    for a in xrange(iterationNum):
        #Don't use fabs. It can be negative.
        z = z * z + coord
        #This is a comparison between complex and int. It probably won't work.
        #You want |Z| which is: z.real ** 2 + z.imag ** 2 > 4
        if abs(z) > 2:
            return False
    return True

def pixel(image,x,y,r,g,b):
   """Place pixel at pos=(x,y) on image, with color=(r,g,b)"""
   image.put("#%02x%02x%02x" % (r,g,b), (y, x))

#here's some example coloring code that may help:
def draw(grid):
    #Create a white image with the size of the grid as the number of pixels
    img = Image.new('RGB', (len(grid), len(grid)), "white")
    pixels = img.load()
    for row in xrange(len(grid)):
        for col in xrange(len(grid[row])):
            if grid[row][col] == True:
                #If that point is True (it's in the set), color it blue
                pixels[row, col] = (0, 0, 255)
    return img

def mandelbrot():
    #you should probably use a square, it's easier to deal with
    #The mandelbrot set fits completely within (-2, 2) and (2, -2)
    #(-200, 200), (200, -200) is way too big!
    TopLeftX = -2; BottomRightX = 2
    TopLeftY = 2; BottomRightY = -2
    #increment should be calculated based on the size of the bounds and the number of pixels
    #For example, if you're between -2 and 2 on the X-Plane, and your image is 400 pixels wide
    #Then your increment = (2 - (-2)) / 400 = 4 / 400 = .01 so that each pixel is 1/400th of the
    #Total width of the bounding area
    increment = 0.01
    maxIt = 100
    w = BottomRightX - TopLeftX
    h = TopLeftY - BottomRightY
    #This should be based on the size of the image, one spot in the area for one pixel
    npArr = np.zeros((w / increment, h / increment), dtype=bool)
    #Use the increment variable from above. It won't work with xrange because that doesn't
    #Support decimals. You probably want to use a while loop or something
    x = -2
    y = 2
    count = 0
    while TopLeftX <= x <= BottomRightX:
        y = 2
        while TopLeftY >= y >= BottomRightY:
            #I recommend using True or False in here (in the set or not)
            #And then do your color calculations as I explained above
            #Saves a lot of memory
            if iterate(x, y, maxIt):
                npArr[x][y] = True
                count += 1
            y -= increment
    #once you've calculated the Trues and Falses, you'd call the draw() function
    #using the npArr as the parameter. I haven't tested the code, so there may
    #be a few bugs, but it should be helpful!
        x += increment
    return npArr

img = draw(mandelbrot())
img.save("mandelbrot.png")
