import pygame as py
class Object:
    def intersect(self, ro:py.Vector3, rd:py.Vector3)->float:
        pass

    def get_color(self)->py.Vector3:
        return self.colorMask
    
    def get_normal(self, minIt:float, ro:py.Vector3, rd:py.Vector3) -> py.Vector3:
        pass