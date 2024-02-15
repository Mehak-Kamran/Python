#single inheritance 
class Car:
    def __init__(self,color):
        self.color=color
    
    @staticmethod
    def start():
        print("car is started....")
    
    @staticmethod
    def stop():
        print("car has stoped.")

class Toyota(Car):
    def __init__(self,type,color):
        super().__init__(color)
        self.type=type

    
    
    



c1=Toyota("crown","orange")
print(c1.type)
print(c1.color)
c1.start()
c1.stop()


