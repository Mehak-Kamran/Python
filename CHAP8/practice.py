#q1
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def avg(self):
        sum=0
         
        for i in self.marks:
            sum= i+sum
        avg=sum/(3)
        print(self.name,"Your avg marks are: ",avg)
       

s1=Student("tony",[88,91,77])
s1.avg()
s2=Student("mark",[78,98,56])
s2.avg()

#2
class Account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no
        print("Your account no is ",self.account_no)

    def debit(self,debit):
        self.balance=self.balance-debit
        print("you debitted rs ",debit,"Remaing balance is ",self.balance)

    def credit(self,credit):
        self.balance=self.balance+credit
        print("you creditted rs ",credit,"Total balance is ",self.balance)
      

    def balanceprint(self):
        
        print("Your balance is rs ",self.balance)


p1=Account(1000,4500067289)
p1.balanceprint()
p1.credit(200)
p1.debit(100)
p1.debit(200)
p1.balanceprint()


            
