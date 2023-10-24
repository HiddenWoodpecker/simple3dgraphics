import pygame as py
import sys
from math import sqrt
from sphere import Sphere
from camera import Camera
from plain import Plain
from scene import Scene
from math import inf
py.init()


W = 800
H = 800
TILE = 15
sc = py.display.set_mode((W,H))
s = py.Surface((W,H))
light = py.Vector3(3,3, 10).normalize()

s.fill((0,0,0))
sc.blit(s,(0,0))
py.display.update()


        
def get_color(v:int, minv:int, maxv:int)->int:
    return max(min(maxv, v) , minv)

clock=py.time.Clock() 
sphere1 = Sphere(py.Vector3(3, 0,0) , 5)
sphere2=  Sphere(py.Vector3(-10, 3,0) , 5)
sphere2.colorMask = py.Vector3(1,2,2)
camera = Camera(py.Vector3(-10,0,0), py.Vector3(1,0,0), py.Vector3(0,0,1))#camera
plain1 = Plain(py.Vector3(0,0,-3), py.Vector3(1,0,0), py.Vector3(0,1,0))
scene = Scene(sphere1, plain1, sphere2)

c = 0
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
        
        keys = py.key.get_pressed()
        camera.move(keys)

        if  keys[py.K_DOWN]:
            camera.change_upguide(-90)
        if keys[py.K_UP]:
            camera.change_upguide(90)
        if keys[py.K_LEFT]:
            camera.change_right(False)
        if keys[py.K_RIGHT]:
            camera.change_right(True)
        
    light = light.normalize()
    ro = camera.get_center()
    for i in range(0,W,TILE):
        for j in range(0,H,TILE):
            x = (i/W)*2 * W/H - 1
            y = (j/H)*2 - 1
            rd = camera.get_dir(x,y).normalize()
            minIt = 10000
            minIt, obj = scene.FMD(ro,rd)
            if obj == None:
                color = (0,0,0)
            elif minIt == -1:
                color = (0,0,0)
            else:
                objColorMask = obj.get_color()
                n = obj.get_normal(minIt, ro, rd)
                n = n.normalize()

                diffuse = max(0, n.dot(light))*0.35
                reflection = (rd - 2*n.dot(rd)*n).normalize()
                spec = max(0, reflection.dot(light))**2
                c = int(( spec+diffuse)*200)
                color = (c//objColorMask.x,c//objColorMask.y,c//objColorMask.z)
            py.draw.rect(sc, color, (i,j,TILE,TILE))
            
    #print(camera.r, camera.upguide, camera.dr)
    #print(camera.upguide,camera.r, camera.upguide.dot(camera.dr))
    #print(camera.upguide)
    light = light.rotate(1, py.Vector3(1,0,1))
    py.display.update()
    sc.fill((0,0,0))
    