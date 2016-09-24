import math
import numpy as np
import scipy.misc as smp
from PIL import PILLOW_VERSION
from PIL import Image

def iterate(x, y, iterationNum):
    z = 0
    coord = complex(x, y)
    while iterationNum:
        #Don't use fabs. It can be negative.
        z = math.fabs(z * z) + coord
        #This is a comparison between complex and int. It probably won't work.
        #You want |Z| which is: z.real ** 2 + z.imag ** 2 > 4
        if z ** 2 > 4:
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
    for row in len(grid):
        for col in len(grid[row]):
            if grid[row][col] == True:
                #If that point is True (it's in the set), color it blue
                pixels[row, col] = (0, 0, 255) 
    return img
            
def mandelbrot():
    #you should probably use a square, it's easier to deal with
    WIDTH = 640; HEIGHT = 480
    #The mandelbrot set fits completely within (-2, 2) and (2, -2)
    #(-200, 200), (200, -200) is way too big!
    TopLeftX = -200; BottomRightX = 200
    TopLeftY = 200; BottomRightY = -200
    #increment should be calculated based on the size of the bounds and the number of pixels
    #For example, if you're between -2 and 2 on the X-Plane, and your image is 400 pixels wide
    #Then your increment = (2 - (-2)) / 400 = 4 / 400 = .01 so that each pixel is 1/400th of the 
    #Total width of the bounding area
    Increment = 5
    maxIt = 100
    w = BottomRightX - TopLeftX
    h = TopLeftY - BottomRightY
    #This should be based on the size of the image, one spot in the area for one pixel
    npArr = np.zeros((w / 0.05, h / 0.05, 3))
    #Use the increment variable from above. It won't work with xrange because that doesn't
    #Support decimals. You probably want to use a while loop or something
    for x in xrange(TopLeftX, BottomRightX, -5):
        for y in xrange(TopLeftY, BottomRightY, -5):
            xnum = x / 100.0
            ynum = y / 100.0
            #I recommend using True or False in here (in the set or not)
            #And then do your color calculations as I explained above
            #Saves a lot of memory!
            if iterate(xnum, ynum, maxIt):
                npArr[xnum, ynum] == [0, 191, 255] # Changes it to blue
            else:
                npArr[xnum, ynum] == [255, 255, 255] # Changes color to white.
                
    #once you've calculated the Trues and Falses, you'd call the draw() function
    #using the npArr as the parameter. I haven't tested the code, so there may
    #be a few bugs, but it should be helpful!
    return npArr

img = smp.toimage(mandelbrot())
img.save("mandelbrot.png")
