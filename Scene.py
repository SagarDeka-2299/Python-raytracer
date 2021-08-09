# -*- coding: utf-8 -*-
"""
Created on Thu May 20 22:30:05 2021

@author: Sagar
"""

class Scene:
    #contains objects,camera,viewport width , viewport height
    def __init__(self, camera,objs,lights,width,height):
        self.camera=camera
        self.objects=objs
        self.width=width
        self.height=height
        self.lights=lights