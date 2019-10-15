#!/usr/bin/python3.6

import math
# Generate main

image = [[0 for item in range(8)] for j in range(8)]
prewittX = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
prewittY = [[1, 1, 1], [0, 0, 0], [-1, -1, -1]]

sobelX = [[-1, 0, 1], [-2, 0, 2], [-1, 0, -1]]
sobelY = [[-1, -2, -1], [0,0,0], [1, 2, 1]]

for x in range(0, 8):
    for y in range(0, 8):
        image[x][y] = abs(x - y)



def printImage(image):
    for x in range(8):
        for y in range(8):
            print('%.3f'%(image[x][y]), end=', ')
        print("")

def applyFilter(image, fil):
    result = image.copy()
    for x in range(1, 7):
        for y in range(1, 7):

            frameVal = 0

            for i in range(-1, 2):
                for j in range(-1, 2):

                    frameVal += image[x+i][y+j] * fil[i+1][j+1]

            result[x][y] = float('%.3f'%(frameVal/9))

    return result

#printImage(image)

gx = applyFilter(image, prewittX)
gy = applyFilter(image, prewittY)

def applyFunction(img1, img2, fun):
    result = [[0 for item in range(8)] for j in range(8)]
    for x in range(8):
        for y in range(8):
            result[x][y] = fun(img1[x][y], img2[x][y])

    return result

def magnitude(imgx, imgy):
    return  applyFunction(imgx, imgy, lambda x, y : pow(pow(x, 2) + pow(y, 2)  , 0.5))
 

def direction(imgx, imgy):
    return applyFunction(imgx, imgy, lambda x, y : math.atan2(y, x))

#g = applyFunction(gx, gy, lambda x, y : pow(pow(x, 2) + pow(y, 2)  , 0.5))

#gDir = applyFunction(gx, gy, lambda x, y : math.atan2(y, x))

#printImage(gDir)

sx = applyFilter(image, sobelX)
sy = applyFilter(image, sobelY)

s = magnitude(sx, sy)
dirS = direction(sx, sy)
printImage(dirS)
