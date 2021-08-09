# -*- coding: utf-8 -*-
"""
Created on Sat May 22 02:40:50 2021

@author: Sagar
"""
from Color import Color
from Vec3 import Vec3
class Light:
    def __init__(self,position=Vec3(0,0,2),color=Color(1,1,1)):
        self.color=color
        self.position=position