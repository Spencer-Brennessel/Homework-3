#!/usr/bin/python3

import math
from copy import deepcopy
# Generate main

image = [[0 for item in range(8)] for j in range(8)]
prewittX = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
prewittY = [[1, 1, 1], [0, 0, 0], [-1, -1, -1]]

sobelX = [[-1, 0, 1], [-2, 0, 2], [-1, 0, -1]]
sobelY = [[-1, -2, -1], [0,0,0], [1, 2, 1]]


checker = []

for i in range(10):
    checker.append([0,0,0,0,0,0,0,0,0,0,40,40,40,40,40,40,40,40,40,40])

for i in range(10):
    checker.append([40,40,40,40,40,40,40,40,40,40,0,0,0,0,0,0,0,0,0,0])


for x in range(0, 8):
    for y in range(0, 8):
        image[x][y] = abs(x - y)



def printImage(image, size=8):
    for x in range(size):
        for y in range(size):
            print('%.1f'%(image[x][y]), end=', ')
        print("")

def applyFilter(image, fil, size=8):
    result = deepcopy(image)
    for x in range(1, size-1):
        for y in range(1, size-1):

            frameVal = 0

            for i in range(-1, 2):
                for j in range(-1, 2):

                    frameVal += image[x+i][y+j] * fil[i+1][j+1]

            result[x][y] = float('%.1f'%(frameVal/9))

    return result

def applyFunction(img1, img2, fun, size=8):
    result = [[0 for item in range(size)] for j in range(size)]
    for x in range(size):
        for y in range(size):
            result[x][y] = fun(img1[x][y], img2[x][y])

    return result

def magnitude(imgx, imgy, size=8):
    return  applyFunction(imgx, imgy, lambda x, y : pow(pow(x, 2) + pow(y, 2)  , 0.5), size)
 

def direction(imgx, imgy, size=8):
    return applyFunction(imgx, imgy, lambda x, y : math.atan2(y, x), size)



#printImage(checker, 20)
cx = applyFilter(checker, prewittX, 20)
cy = applyFilter(checker, prewittY, 20)

c = magnitude(cx, cy, 20)


def cmatrix(imgx, imgy, size=20, nbhd=7):

    cmatrix = []

    for i in range(0, size-nbhd+1):
        for j in range(0, size-nbhd+1):

            cx = 0
            cy = 0
            cxy= 0

            for x in range(i, i+nbhd):
                for y in range(j, j+nbhd):
                    cx += imgx[x][y]*imgx[x][y]
                    cy += imgy[x][y]*imgy[x][y]
                    cxy+= imgx[x][y]*imgy[x][y]

            cx = int(cx)
            cy = int(cy)
            cxy= int(cxy)

            cmatrix.append([[cx, cxy], [cxy, cy]])

    return cmatrix


def printCMatrix(cmatrix, nbhd=7, size=20):
    
    i = 0
    while i < pow(size-nbhd+1, 2):
        for j in range(size-nbhd+1):
            print(cmatrix[i+j][0], end=";")
        print(" ")
        for j in range(size-nbhd+1):
            print(cmatrix[i+j][1], end=";")
        print("\n")
        i += size-nbhd+1


cmatrix = cmatrix(cx, cy)
printCMatrix(cmatrix)



#printImage(image)

gx = applyFilter(image, prewittX)
gy = applyFilter(image, prewittY)


g = applyFunction(gx, gy, lambda x, y : pow(pow(x, 2) + pow(y, 2)  , 0.5))

gDir = applyFunction(gx, gy, lambda x, y : math.atan2(y, x))

#printImage(gDir)

sx = applyFilter(image, sobelX)
sy = applyFilter(image, sobelY)

s = magnitude(sx, sy)
dirS = direction(sx, sy)
