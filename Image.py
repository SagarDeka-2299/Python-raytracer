from Color import Color 
class Image:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.pixels=[[Color(0,0,0) for _ in range(width)]for _ in range(height)] #default color black
        
    def set_pixel(self,row,column,color):
        #assign color to given index
        self.pixels[row][column]=color
        
    def write_image_ppm(self,filename):
        
        with open(filename,"w") as image_file:
            image_file.write("P3 {} {}\n255\n".format(self.width, self.height))
            for rows in self.pixels:
                for color in rows:
                    image_file.write("{} {} {} ".format(color.to_8bit().r,color.to_8bit().g,color.to_8bit().b))
                image_file.write("\n")