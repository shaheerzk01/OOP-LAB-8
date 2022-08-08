# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 15:06:22 2021

@author: 21A-003-se
"""
import math
class RegularPolygon:
    def __init__(self, n=3, side=1, x=0, y=0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y
        
    def getN(self):
        return self.__n
    def setN(self, n):
        self.__n = n
    
    def getSide(self):
        return self.__side
    def setSide(self, side):
        self.__side = side
    
    def getX(self):
        return self.__x
    def setX(self, x):
        self.__x = x
    
    def getY(self):
        return self.__y
    def setY(self, y):
        self.__y = y
    
    def getParameter(self):
        return self.__n * self.__side
    
    def getArea(self):
        a = self.__n * (self.__side)**2
        b = 4 * math.tan(math.pi/self.__n)
        return a/b
    
def main():
    r1 = RegularPolygon()
    r2 = RegularPolygon(6, 4)
    r3 = RegularPolygon(10, 4, 5.6, 7.8)
    print(r1.getParameter(), r1.getArea())
    print(r2.getParameter(), r2.getArea())
    print(r3.getParameter(), r3.getArea())
main()