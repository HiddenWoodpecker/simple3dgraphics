import pygame as py
import numpy
from math import inf
from object import Object
EPSILON = 0.00001

MAX_RENDER_DIST = 10000
class Plain (Object):
    def __init__(self, orig:py.Vector3, v1:py.Vector3, v2:py.Vector3) -> None:
        self.orig = orig
        self.v1 = v1
        self.v2 = v2
        #self.matrix = [[-self.orig.x, -self.orig.y, -self.orig.z],
         #              [self.v1.x-self.orig.x, self.v1.y-self.orig.y, self.v1.z-self.orig.z],
          #             [self.v2.x-self.orig.x, self.v2.y-self.orig.y, self.v2.z-self.orig.z]]
        #self.n = py.Vector3(self.matrix[1][1]*self.matrix[2][2] -self.matrix[1][2]*self.matrix[2][1],
         #                   -1*(self.matrix[1][0]*self.matrix[2][2] - self.matrix[1][2]*self.matrix[2][0]),
          #                  self.matrix[1][0]*self.matrix[2][1] -self.matrix[1][1]*self.matrix[2][0]
           #                  ).normalize()
        #self.d = -self.matrix[0][0]*self.n.x+ self.matrix[0][1]*self.n.y - self.matrix[0][2]*self.n.z
        self.n = py.Vector3(0,0,1)
        self.d = -3
        self.colorMask = py.Vector3(1,10,10)
    
    def intersect(self, ro:py.Vector3, rd:py.Vector3)->float:
        q = rd.dot(self.n)
        if q < EPSILON:
            return -1

        t = (-self.d - self.n*ro)/q
        if t > MAX_RENDER_DIST or t <= 0:
            return - 1
        return t
    
    def get_color(self) -> py.Vector3:
        return self.colorMask
    
    def get_normal(self, minIt:float, ro:py.Vector3, rd:py.Vector3) -> py.Vector3:
        return self.n