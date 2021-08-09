from Vec3 import Vec3
class Color(Vec3):
    r,g,b=0,0,0
    def __init__(self,r=None,g=None,b=None):
        if(r!=None and g!=None and b!=None):
            super().__init__(r,g,b)
            self.r=self.x
            self.g=self.y
            self.b=self.z
        elif(r!=None and g==None and b==None):
            #if vec3 as an argument
            super().__init__(r.x,r.y,r.z)
            self.r=self.x
            self.g=self.y
            self.b=self.z
            
    #keep value between 0,1
    def clamp(self):
        rr=max(min(self.r,1),0)
        rg=max(min(self.g,1),0)
        rb=max(min(self.b,1),0)
        return Color(rr,rg,rb)
    
    #make 0 to 255
    def to_8bit(self):
        
        return Color(round(self.clamp().x*255),round(self.clamp().y*255),round(self.clamp().z*255))
    
    @classmethod
    def from_hex(cls,hex_code):
        rr=int(hex_code[1:3],16)/255.0
        rg=int(hex_code[3:5],16)/255.0
        rb=int(hex_code[5:7],16)/255.0
        return Color(rr,rg,rb)
