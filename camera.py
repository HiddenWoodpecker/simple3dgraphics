import pygame as py


class Camera:

    def __init__(self, origin:py.Vector3, r:py.Vector3, upguide: py.Vector3) -> None:
        self.origin = origin
        self.r = r.normalize()
        self.upguide = upguide.normalize()
        self.dr = self.r.cross(self.upguide).normalize()
        

    def change_right(self, right:bool)->None:
        if right:
            self.r += 0.1*(self.dr)
        else:
            self.r -= 0.1*self.dr
        self.r = self.r.normalize()
        self.dr = self.r.cross(self.upguide).normalize()


    def change_upguide(self, angle)->None:
        pass

    def zoom_in_out(self, dir=True)->None:
        if dir:
            self.r += self.r*0.1
        elif not dir and self.r.length() > 0.3:
            self.r -= self.r*0.1
        


    def move(self,keys)->None:
        if keys[py.K_LCTRL]:
            self.origin -= self.upguide
        if keys[py.K_SPACE]:
            self.origin += self.upguide
        if  keys[py.K_w]:
            self.origin += self.r
        if  keys[py.K_s]:
            self.origin -= self.r   
        if  keys[py.K_d]:
            self.origin += self.dr
        if  keys[py.K_a]:
            self.origin -= self.dr
        if  keys[py.K_q]:
            self.zoom_in_out(True)
        if  keys[py.K_e]:
            self.zoom_in_out(False)
    
    def get_center(self)->py.Vector3:
        return self.origin
    
    def get_right(self)->py.Vector3:
        return self.dr
    def get_upguide(self)->py.Vector3:
        return self.upguide

    def get_dir(self, x:float, y:float) ->py.Vector3:
        return (self.r + x*self.dr + y*self.upguide).normalize()

