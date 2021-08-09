# -*- coding: utf-8 -*-
"""
Created on Thu May 20 20:35:59 2021

@author: Sagar
"""


from Vec3 import Vec3
class Obj:
   
    def __init__(self,pos=Vec3(0,0,0),rot=Vec3(0,0,0),scal=Vec3(1,1,1)):

        self.Position=Vec3(pos.x,pos.y,pos.z)

        self.Rotation=Vec3(rot.x,rot.y,rot.z)
        

        self.Scale=Vec3(scal.x,scal.y,scal.z)


