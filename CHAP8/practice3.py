#class method
class person:
    name="Roshan"
    @classmethod
    def changename(cls,name):
        cls.name=name

p1=person()
p1.changename("eddi")
print(p1.name)
print(person.name)

#property
class result:
    def __init__(self,cg,os,cc):
        self.cg=cg
        self.os=os
        self.cc=cc
        #self.per=str((cg+os+cc)/3)+"%"
    @property
    def percentage(self):
        return str((self.cg+self.os+self.cc)/3)+"%"


p1=result(71,71,88)
print(p1.percentage)
p1.os=91
print(p1.percentage)


    

