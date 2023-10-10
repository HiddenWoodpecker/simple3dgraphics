import pygame as py
from math import sqrt

class Sphere:
    def __init__(self, center: py.Vector3, radius:int) -> None:
        self.center = center
        self.radius = radius
        self.colorMask = py.Vector3(3,2,2)
    
    def intersect(self, origin:py.Vector3, dir:py.Vector3)->float:
        op = origin - self.center #Перемещаемся с систему координат с началом в точке центра сферы
        b = 2*py.Vector3.dot(dir, op)
        c = 4*((py.Vector3.dot(op, op)) - self.radius **2)
        d = b*b - c
        if d <= 0 :
            return -1
        d = sqrt(d)
        z = (-b - d) / 2
        if (z > 0):
            return z
        return -1        
 