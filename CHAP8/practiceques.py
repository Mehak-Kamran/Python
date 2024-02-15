#q1
class circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        areaofcircle= 3.142*(self.radius**2)
        return areaofcircle
    
    def perimeter(self):
        per=2*3.142*(self.radius)
        return per

c=circle(21)
print(c.area())
print(c.perimeter())

#2
class employee:
    def __init__(self,role,dep,sal):
        self.role=role
        self.dep=dep
        self.sal=sal

    def showdetails(self):
        print("name:",self.name)
        print("age:",self.age)
        print("Role:",self.role)
        print("Dep:",self.dep)
        print("Salary:",self.sal)

class Engineer(employee):
    def __init__(self,name,age,role,dep,sal):
        self.name=name
        self.age=age
        super().__init__(role,dep,sal)

    


eng=Engineer("bila",26,"data analyst","finance",10000)
eng.showdetails()


#3
class order():
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,o2):
        return self.price>o2.price
    

    
o1=order("pasta",3000)
o2=order("fish",2000)
print(o1>o2)
