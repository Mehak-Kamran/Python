# #single inheritance 
# class Car:
#     def __init__(self,color):
#         self.color=color
    
#     @staticmethod
#     def start():
#         print("car is started....")
    
#     @staticmethod
#     def stop():
#         print("car has stoped.")

# class Toyota(Car):
#     def __init__(self,type,color):
#         super().__init__(color)
#         self.type=type


# c1=Toyota("crown","orange")
# print(c1.type)
# print(c1.color)
# c1.start()
# c1.stop()

#multi level inheritance

# class GrandFather:
#     def __init__(self,qualities):
#         self.qualities=qualities
    
#     @staticmethod
#     def gf():
#         print("grand father")

# class Father(GrandFather):
#     def __init__(self,name,qualities):
#         self.name=name
#         super().__init__(qualities)

#     @staticmethod
#     def f():
#         print("father")

# class son(Father):
#     def __init__(self,name,qualities):
#         self.name=name
#         super().__init__(name,qualities)

# fat=son("son","kindness")
# fat.gf()
# fat.f()
# print(fat.qualities)

#multiple inheritance

class father:
    def __init__(self,name):
        self.name=name
    
    @staticmethod
    def fatherfamily():
        print("father family")

class mother:
    def __init__(self,lname):
        self.lname=lname
    
    @staticmethod
    def motherfamily():
        print("mother family")

class daughter(father,mother):
    def __init__(self,name,lname):
        print("daughter is confident")
        father.__init__(self,name)
        mother.__init__(self,lname)


        
d1=daughter("father","mother")
d1.motherfamily()
d1.fatherfamily()
print(d1.name)
print(d1.lname)

    


