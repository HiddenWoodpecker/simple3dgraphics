import pygame as py
from math import sqrt
from object import Object

class Sphere (Object):
    def __init__(self, center: py.Vector3, radius:int) -> None:
        self.center = center
        self.radius = radius
        self.colorMask = py.Vector3(3,2,2)
    
    def intersect(self, ro:py.Vector3, rd:py.Vector3)->float:
        op = ro - self.center #Перемещаемся с систему координат с началом в точке центра сферы
        b = 2*py.Vector3.dot(rd, op)
        c = 4*((py.Vector3.dot(op, op)) - self.radius **2)
        d = b*b - c
        if d <= 0 :
            return -1
        d = sqrt(d)
        z = (-b - d) / 2
        if (z > 0):
            return z
        return -1        
    
    def get_color(self)->py.Vector3:
        return self.colorMask
    
    def get_normal(self, minIt:float, ro:py.Vector3, rd:py.Vector3) -> py.Vector3:
        intersectionPoint = ro + minIt *rd
        n = -(intersectionPoint - self.center)
        return n