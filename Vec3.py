class Vec3:
    x,y,z=0,0,0

    def __init__(self,x,y=None,z=None):
        if(x!=None and y!=None and z!=None):
            self.x=x
            self.y=y
            self.z=z
        elif(x!=None and y==None and z==None):
            self.x=x[0]
            self.y=x[1]
            self.z=x[2]
       
    def magnitude(self):
        return ((self.x*self.x)+(self.y*self.y)+(self.z*self.z))**(0.5)

    def normalized(self):
        #gives unit vector
        xr=self.x/self.magnitude()
        yr=self.y/self.magnitude()
        zr=self.z/self.magnitude()
        unit_vec=Vec3(xr,yr,zr)
        return unit_vec    
    
    
    def dot(self,othervec):
        #self.othervec=(x1 x2)+(y1 y2)+(z1 z2)
        return (self.x*othervec.x)+(self.y*othervec.y)+(self.z*othervec.z)
    
    
    def cross(self,other):
        #self X othervec=[(y1 z2 - z1 y2),(z1 x2 - x1 z2),(x1 y2 - y1 x2)]
        xr=self.y*other.z-self.z*other.y
        yr=self.z*other.x-self.x*other.z
        zr=self.x*other.y-self.y*other.x
        cross_product=Vec3(xr, yr, zr)
        return cross_product
    
    def __mul__(self,scalar):
        #scalar value must be put after *
        xr=self.x*scalar
        yr=self.y*scalar
        zr=self.z*scalar
        result_vec=Vec3(xr,yr,zr)
        return result_vec
    
    def __rmul__(self,scalar):
        #as multiplication with scalar commutative
        return self.__mul__(scalar)
    
    def __truediv__(self,scalar):
        #scalar value must be put after *
        xr=self.x/scalar
        yr=self.y/scalar
        zr=self.z/scalar
        result_vec=Vec3(xr,yr,zr)
        return result_vec
    
    def __add__(self,othervec):
        xr=self.x+othervec.x
        yr=self.y+othervec.y
        zr=self.z+othervec.z
        result_vec=Vec3(xr,yr,zr)
        return result_vec
    def __sub__(self,othervec):        
        result_vec=self.__add__(othervec.__mul__(-1))
        return result_vec
        
    def project_on(self, othervec):
        result_vec=othervec.normalized()*self.dot(othervec.normalized())
        return result_vec

        
    def __str__(self):
        return "{},{},{}".format(self.x,self.y,self.z)
    









