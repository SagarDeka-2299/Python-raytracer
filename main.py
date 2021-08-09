# -*- coding: utf-8 -*-
"""
Created on Thu May 20 02:09:37 2021

@author: Sagar
"""
from RenderEngine import RenderEngine
from Image import Image
from Obj import Obj
from Sphere import Sphere
from Vec3 import Vec3
from Scene import Scene
from Light import Light
from Color import Color
from Material import Material

def main():
    WIDTH=320
    HEIGHT=200
    image=Image(WIDTH, HEIGHT)
    
    #camera satup
    cam_pos=Vec3(0,0,-1)
    camera=Obj(cam_pos,Vec3(0,0,0),Vec3(0,0,0))
    
    #sphere setup
    sp_pos=Vec3(0,0,.1)
    rad=.5
    color="#FF0F0F"

    material=Material(Color.from_hex(color))
    sphere=Sphere(material,sp_pos, Vec3(0,0,0), rad)
    objs=list()
    objs.append(sphere)
    
    #light setup
    
    light_pos=Vec3(-.1,-1.3,-2)
    light_color="FFFF00"
    light=Light(light_pos,Color.from_hex(light_color))
    lights=list()
    lights.append(light)
    
    
    
    #scene setup
    scene=Scene(camera,objs,lights,WIDTH,HEIGHT)
    engine=RenderEngine()
    image=engine.render(scene)
    
    image.write_image_ppm("my_image.ppm")

if(__name__=="__main__"):
    main()