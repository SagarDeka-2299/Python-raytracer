# -*- coding: utf-8 -*-
"""
Created on Thu May 20 20:35:59 2021

@author: Sagar
"""

from Obj import Obj
from Vec3 import Vec3


class Sphere(Obj):
    
    def __init__(self,material,pos=Vec3(0,0,0),rot=Vec3(0,0,0),rad=1):
                

        super().__init__(pos,rot,Vec3(rad,rad,rad))
        self.Radius=rad
        self.material=material
    
    def intersects(self, ray):
        #detail about ray interaction with the sphere
        """
        returns intersaction distance if interacts with given array
        else returns -1
        """
        
        #Vec3
        sphere_to_ray=ray.origin-self.Position
        
        #scalar
        b= 2* ray.direction.dot(sphere_to_ray)
        #scalar
        c=sphere_to_ray.dot(sphere_to_ray)-(self.Radius**2)
        
        D=b*b-4*c
        
        if(D>=0):
            dist=(-1*b-(D**0.5))/2
            if(dist>0):
                return dist
            
        return -1
    def normal(self,surface_point):
        return (surface_point-self.Position).normalized()