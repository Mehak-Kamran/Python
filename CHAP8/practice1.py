#delete an object

# class tree:
#     def __init__(self,leaves,branch):
#         self.leaves=leaves
#         self.branch=branch

# t1=tree("palmtreeleaves","brown")
# del t1
# print(t1.leaves,t1.branch)

#private class

# class Account:
#     def __init__(self,accountno,accountpass):
#         self.accountno=accountno
#         self.__accountpass=accountpass

# acc=Account("45678","abc87")
# print(acc.accountpass)

#u can also make private function and private variable 

#inheritance

class laptop:
    @staticmethod
    def start():
        print("laptop is started")
    
    @staticmethod
    def shutdown():
        print("laptop is shutdown")


class HP(laptop):
    def __init__(self,model):
        self.model=model

    
l1=HP("Probook")
l1.start()
