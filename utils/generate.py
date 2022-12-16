from random import random
from math import cos, sin, pi

def lerp(a, b, t):
    return a + (b-a)*t

def genUniformRectangle(xStart, xEnd, yStart, yEnd, count):
    '''Generuje count punktów z prostokąta: xStart < x < xEnd i yStart < y < yEnd'''
    return [[lerp(xStart, xEnd, random()), lerp(yStart, yEnd, random())] for _  in range(count)]

def genUniformRectangle(x, y, radius, count):
    '''Generuje count punktów na okregu o środku w (x,y) i promieniu radius'''
    return [[x + radius*cos(angle), y + radius*cos(angle)] for angle in [2*pi*random() for _  in range(count)]]

def genUniformOnRectangle(lowerLeft, upperRight, count):
    '''Generuje count punktów na prostokącie o lewym dolnym punkcie w lowerLeft i prawym gowrnym upperRight.'''
    ll, ur, arr = lowerLeft, upperRight, [[] for _ in range(count)]
    for i in range(count):
        s = random.randint(0, 3)
        t = random.random()

        # dolna krawędz
        if s == 0:
            arr[i] = [lerp(ll[0], ur[0], t), ll[1]]
        
        # prawa krawędz
        if s == 1:
            arr[i] = [ur[0], lerp(ll[1], ur[1], t)]
        
        # górna krawędz
        if s == 2:
            arr[i] = [lerp(ll[0], ur[0], t), ur[1]]
        
        # lewa krawędz
        if s == 3:
            arr[i] = [ll[0], lerp(ll[1], ur[1], t)]
    
    return arr

def genUniformOnSquare(side, sideCount, diagonalCount):
    '''Generuje sideCount punktów na bokach kwadratu zawierających się w OX oraz
       OY oraz diagonalCount na przekątnych kwadratu o boku side'''
    arr = [[] for _ in range(2*(sideCount + diagonalCount))]

    for i in range(sideCount):
        arr[i] = [random.random()*side, 0]
    
    for i in range(sideCount):
        arr[i + sideCount] = [0, random.random()*side]
    
    for i in range(diagonalCount):
        x = random.random() * side
        arr[i + 2*sideCount] = [x, x]

    for i in range(diagonalCount):
        x = random.random() * side
        arr[i + 2*sideCount + diagonalCount] = [x, side - x]
    
    arr.append([0, 0])
    arr.append([side, 0])
    arr.append([0, side])
    arr.append([side, side])

    return arr