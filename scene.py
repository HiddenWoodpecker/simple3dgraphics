from object import Object
import pygame as py
from math import inf
class Scene:

    def __init__(self, *obj:[Object]):
        self.objects = obj
    
    def FMD(self, ro:py.Vector3, rd:py.Vector3) -> (float, Object):
        minDist = 10000
        minDistObj = None
        for i in range(len(self.objects)):
            tmp = self.objects[i].intersect(ro,rd)
            if tmp < minDist and tmp != -1:
                minDist = tmp
                minDistObj = self.objects[i]
        if minDist >= 10000:
            minDist = -1
        return (minDist, minDistObj)

