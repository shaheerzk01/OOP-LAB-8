# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 14:56:44 2021

@author: 21A-003-se
"""

class BMI:
    def __init__(self, name, age, weight, height):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__height = height
        
    def get_name(self):
        return self.__name
    
    def get_BMI(self):
        a = self.__weight/2.205
        b = self.__height/39.37
        BMI = a/(b**2)
        return BMI
    
    def status(self):
        if self.get_BMI() < 18.5:
            print("Under weight")
        elif self.get_BMI() > 18.5 and self.get_BMI() < 24.9:
            print("Normal")
        elif self.get_BMI() > 25 and self.get_BMI() < 29.9:
            print("Over weight")
        elif self.get_BMI() > 30.0:
            print("Obese")
            
def main():
    p1 = BMI("John Doe", 18, 145, 70)
    p2 = BMI("Peter King", 50, 215,70)
    print(p1.get_BMI())
    p1.status()
    print(p2.get_BMI())
    p2.status()
main()