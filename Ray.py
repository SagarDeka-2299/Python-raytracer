# -*- coding: utf-8 -*-
"""
Created on Thu May 20 22:26:52 2021

@author: Sagar
"""

class Ray:
    # has origin and direction
    def __init__(self,origin,direction): #(Vec3, Vec3)
        self.origin=origin
        self.direction=direction