#polymorphism
#opertor overloading
#dander function 
#__add__ .......etc

class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def printing(self):
        print(self.real,"i+",self.img,"j")

    def __add__(self,c1):
        newreal=self.real+c1.real
        newimg=self.img+c1.img
        return complex(newreal , newimg)

c=complex(1,3)
c.printing()
c1=complex(2,6)
c1.printing()
# ans=c.add(c1)
# ans.printing()

ans=c+c1
ans.printing()

