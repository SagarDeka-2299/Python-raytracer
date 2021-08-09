# -*- coding: utf-8 -*-
"""
Created on Sat May 22 02:43:06 2021

@author: Sagar
"""
from Color import Color
class Material:
    def __init__(self,color=Color(1,0,1),ambient=0.05,diffuse=2,specular=.85):
        self.color=color
        self.ambient=ambient
        self.diffuse=diffuse
        self.specular=specular
    def color_at(self,position):
        return self.color
         