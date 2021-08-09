# -*- coding: utf-8 -*-
"""
Created on Thu May 20 22:36:03 2021

@author: Sagar
"""
from Image import Image
from Ray import Ray
from Vec3 import Vec3
from Color import Color
from Material import Material

class RenderEngine:
    
    
    def render(self,scene):
        
        # takes scene and trace ray
        #return image obj containing pixel array
        width=scene.width
        height=scene.height
        
        aspect_ratio=float(width/height)
        
        x0=-1.0
        x1=1.0
        y0=-1.0/aspect_ratio
        y1=1.0/aspect_ratio
        
        xstep=(x1-x0)/(width)
        ystep=(y1-y0)/(height)
        
        camera=scene.camera
        pixels=Image(width,height) #pixel array
        
        #iterate for each pixel
        for j in range(height):
            y=y0+j*ystep
            for i in range(width):
                x=x0+i*xstep
                ray=Ray(camera.Position,(Vec3(x,y,0)-camera.Position).normalized())
                pixels.set_pixel(j,i,self.ray_trace(ray,scene))
        return pixels
    def ray_trace(self,ray,scene):
        color=Color(0,0,0)
        # find neares object hit
        dist_hit,obj_hit=self.find_nearest(ray,scene)# returns distance, obj hit 
        if(obj_hit is None):
            return color
        hit_pos=ray.origin+ray.direction*dist_hit
        #normal at hit Position
        hit_normal=obj_hit.normal(hit_pos)
        
        color+=self.color_at(obj_hit,hit_pos,hit_normal,scene)
        return Color(color)
        
    def find_nearest(self, ray, scene):
        dist_min=None
        obj_hit=None
        for obj in scene.objects:
            dist=obj.intersects(ray)
            if(dist!=-1 and (obj_hit is None or dist<dist_min)):
               dist_min=dist
               obj_hit=obj
               
        return (dist_min,obj_hit)
    def color_at(self,obj_hit,hit_pos,hit_normal,scene):
        specular_k=5
        material=obj_hit.material
        obj_color=material.color_at(hit_pos)
        to_cam=scene.camera.Position - hit_pos
        color=material.ambient*Color.from_hex("#000000")
        # diffuse shading
        for light in scene.lights:
            to_light=Ray(hit_pos, (light.position-hit_pos).normalized())
            color+=obj_color*material.diffuse*max(hit_normal.dot(to_light.direction),0)
            
        #specular shading
        half_vector=(to_light.direction+to_cam).normalized()
        color+=light.color*material.specular*max(hit_normal.dot(half_vector),0)**specular_k
        return Color(color)
        
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            